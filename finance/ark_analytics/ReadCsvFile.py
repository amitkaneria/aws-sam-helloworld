import csv
import requests
from datetime import datetime
from dateutil.parser import parse
from UploadCsvFile import insert_vendor
from datetime import datetime
import logging
import boto3
from botocore.exceptions import ClientError
import platform

'''
Need following resources
- S3 bucket
- policy that allows lambda to upload to S3
- POSTGRES table
- policy that allows lambda to update data to POSTGRES DB

TABLESPACE "ARK_Analytics";

ALTER TABLE public."ETF_Holdings"
OWNER to postgres;

## Query to find all investments by fund, date
SELECT fund, date, sum(weight), sum(marketvalue) FROM public."ETF_Holdings"
group by fund, date
order by fund, date

## Query to find changes in holding of a security by ticker
SELECT a.company, a.shares, a.marketvalue, a.weight, a.closing_price, b.shares,
b.marketvalue, b.weight, b.closing_price
FROM public."ETF_Holdings" as a, public."ETF_Holdings" as b where a.date = '2021-01-08' and b.date='2021-01-15'
and a.ticker = b.ticker and a.ticker='TSLA'

## Query to find changes in holding of a security by ticker, with difference
SELECT a.company, a.shares, a.marketvalue, a.weight, a.closing_price, b.shares,
b.marketvalue, b.weight, b.closing_price,
(b.shares-a.shares) as diff_shares,
(b.marketvalue - a.marketvalue) as diff_marketvalue,
(b.weight - a.weight) as diff_weight,
(b.closing_price - a.closing_price) as diff_closing_price
FROM public."ETF_Holdings" as a, public."ETF_Holdings" as b where a.date = '2021-01-08' and b.date='2021-01-15'
and a.ticker = b.ticker and a.ticker='TSLA'

## with all scripts
SELECT a.ticker, a.company,
a.shares as old_shares, b.shares as new_shares, (b.shares-a.shares) as diff_shares,
a.marketvalue as old_market_value, b.marketvalue as new_market_value, (b.marketvalue - a.marketvalue) as diff_marketvalue,
a.weight as old_weight, b.weight as new_weight, (b.weight - a.weight) as diff_weight,
b.closing_price as new_closing_price, a.closing_price as old_closing_price, (b.closing_price - a.closing_price) as diff_closing_price
FROM public."ETF_Holdings" as a, public."ETF_Holdings" as b where a.date = '2021-01-08' and b.date='2021-01-15'
and a.ticker = b.ticker
order by b.weight desc


SELECT a.company, 
a.shares as Old_Shares, b.shares as New_Shares, (b.shares-a.shares) as Diff_Shares,
a.marketvalue as Old_Market_Value, b.marketvalue as New_Market_Value, (b.marketvalue - a.marketvalue) as Diff_Market_Value,
a.weight as Old_Weight, b.weight as New_Weight, (b.weight - a.weight) as Diff_Weight,
a.closing_price as Old_Closing, b.closing_price as New_Closing, (b.closing_price - a.closing_price) as Diff_Closing_Price
FROM public."ARK" as a, public."ARK" as b where a.date = '2021-01-28' and b.date='2021-01-29'
and a.fund = b.fund and a.fund = 'ARKK' and a.ticker = b.ticker
order by b.weight desc

## update stock price query
update public."ETF_Holdings"
set closing_price = marketvalue/shares

'''

def download_file(fund_name, url, file_to_be_processed):
    r =requests.get(url)
    with open(file_to_be_processed,'wb') as f:
        f.write(r.content)
    # upload()

def validate(date_text):
    try:
        datetime = parse(date_text)
        return True
    except ValueError:
        return False


def process_file(fund_name, file_to_be_processed):
    with open(file_to_be_processed) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        total_lines = 0
        valid_lines = 0
        for row in csv_reader:
            if total_lines == 0:
                print(f'Column names are {", ".join(row)}')
                total_lines += 1
            else:
                if(validate(row[0])):
                    # print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    insert_vendor(row[0], row[1], row[2], row[3], row[4], int(float(row[5])), row[6], row[7])
                    valid_lines += 1
                else:
                    print(f'### INVALID LINE ==> {row[0]}')
                total_lines += 1
        print('=================================')
        print(f'PROCESSED {valid_lines}/{total_lines} lines. ')

funds_config = {
    "ARKK": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv",
    "ARKG": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv",
    "ARKQ": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv",
    "ARKW": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv",
    "ARKF": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv",
    "PRNT": "https://ark-funds.com/wp-content/fundsiteliterature/csv/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv",
    "IZRL": "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv",
}


def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    bucket = ''

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == '__main__':
    # datetime = datetime.today().strftime('%Y-%m-%d')
    datetime = '2021-03-11'

    for key in funds_config:
        fund_name = key
        url = funds_config.get(fund_name)

        base_dir = '/tmp/'
        if platform.system() == 'Windows':
            base_dir = 'C:\\Users\\amitk\\Downloads\\ARK\\'
        print(f'### BaseDir : {base_dir}')
        file_to_be_processed = base_dir+fund_name+'_'+datetime+'.csv'

        print(f'### processing : {fund_name} for DATE: {datetime}')
        print(f'URL: {url}, file: {file_to_be_processed}')
        #download_file(fund_name, url, file_to_be_processed)
        process_file(fund_name, file_to_be_processed)