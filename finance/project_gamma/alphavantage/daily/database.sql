-- Table: public.Tech_Daily

-- DROP TABLE public."Tech_Daily";

CREATE TABLE public."Tech_Daily"
(
    ticker text COLLATE pg_catalog."default" NOT NULL,
    date date NOT NULL,
    stochs_slowk double precision,
    stochs_slowd double precision,
    stochs_delta double precision,
    open money,
    high money,
    low money,
    close money,
    volume bigint,
    ema8 money,
    ema12 money,
    ema200 money,
    rsi double precision,
    CONSTRAINT "Tech_Daily_pkey" PRIMARY KEY (ticker, date)
)

TABLESPACE "Gamma";

ALTER TABLE public."Tech_Daily"
    OWNER to postgres;


-- Table: public.Signals

-- DROP TABLE public."Signals";

CREATE TABLE public."Signals"
(
    ticker text COLLATE pg_catalog."default" NOT NULL,
    date date NOT NULL,
    buy_sell text COLLATE pg_catalog."default",
    method text COLLATE pg_catalog."default" NOT NULL,
    note text COLLATE pg_catalog."default",
    reco_price money,
    price_1week money,
    analysis_1week text COLLATE pg_catalog."default",
    price_2week money,
    analysis_2week text COLLATE pg_catalog."default",
    CONSTRAINT "Signals_pkey" PRIMARY KEY (ticker, date, method)
)

TABLESPACE "Gamma";

ALTER TABLE public."Signals"
    OWNER to postgres;


watchlist
ticker
full_run
last_run
industry
