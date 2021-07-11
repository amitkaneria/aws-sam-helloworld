##Client_Id:TMFGIHQ7NBULNNLAPRMDVSTKTMNVBDUF
##Callback URL: http://localhost:8080/td

# https://api.tdameritrade.com/v1/oauth2/token
#
# grant_type=authorization_code, refresh_token
# refresh_token=
# access_type=offline (only used for refresh_token)
# code= (required for authorization_code grant, code received in callback URL)
# client_id = TMFGIHQ7NBULNNLAPRMDVSTKTMNVBDUF
# redirect_url=http://localhost:8080/td

import requests

x = requests.get('https://api.tdameritrade.com/v1/oauth2/token?grant_type=authorization_code&code=E+MejqbKCzpJK+gZEjngIHcfZ0zzm/W0Qf6FlryWSk/py/YMgpdS6KZgVXhyJx/cxMS/56uVNdRGAwtN5x0dEsoNaqrDtkHq1N/K7xsAMa/wsYbakuSu4u8nqW+w1exQobHSCspzkD96wmQvJWUEOzOT8q7QCce76CdSciAjcsysf5zVEqjXD5KYk+QffXtQR7k/StnIwJT73D5d6KSmOxsN7Ty4MJnzUbbUPI1DsqSWDP/V47L9veDQbQyOMMAlXUSBno0EG/blwASZ0NqXOxUva8caGLCUnlvVUvxbyoda9RqO1EDfASXwCv2rq7hTA7Q8ldC5eAi4ak9kwvLJyPiEakeqA69AiWNRm//wo4UDPGFbJr0ByJPrV4YYwAM2xpqsfH6apqHMD3btRGxRj+gPk4VgxBfJynG4/IRZI9XKfYGKfda0oerH69d100MQuG4LYrgoVi/JHHvlt8+oVLLfBrJuIwmqUELf3Ri85Sr7XYoy4rX6kz/dFd7WyaekJE2ETaCPnbu3FUAZDoTl1+JLENG8KGKcnI2pPgV98moxAnKzCNauly1rEWmvzk57+OVOL3+1AuxpMhYsk31d4l6yRLWdnVCXdYk1ulIF6an0EshSAMnNI3lYuaiTyepLYrxLy5UXzfOlcGfh5iv5Snx/B5T/8oHs9HtpDwExYDZFVxndS80fzRBnjsXeQtyUoTSFM92Po2dxgVwPZOmktKSEkryvHeJeImGCXLPt3D6sgd1awORpul+FgnB6Ala5NMLxhigBk+46346fGdnWo5U+V26sj91FBZiY2kuyfm1p84EmWYZytnaGADb49eRPjZOjPWR/ZMaEPC8+5GakNUJ+xO8Z8nAmWjV6LXclW2ANmMmEPNSzcH27arMQLJZJb0kOUeItnpo=212FD3x19z9sWBHDJACbC00B75E&redirect_url=http://localhost:8080/td')
print(x.status_code)

# 5iI0d3/R9TsydruiZo0n8unZxeKnX6vPw3A/bzXdmTYyXauMx4NcQcm1k2VA4YDQNbHqJqIF+POEktV7SZRXibh6HxmHWSTjlGY8CI9NtcD9ftiSfEaq7LMpxLqRnamuvsZ5hgGZ8gZTgplhBeA33qIWd2vGlDcLOH0OtEFfm/R2dwhY4hBe4f/LrkTo0hhDv9wdrctU8Z1s/xcvzPXT7cB3HtMrjGDO9fVgK5BBaaSM6qUmRRJ18mDe9kDHn922v5BpAbit+SRM/BT4f23AgY8kKtCInkhRK9WDX3MFiwHsr2hgnwf5rDOKlO1CKCU2tXoCk8N5ngswApXOxev9fmNn5I5zF2rLaHVFAvhBaTC4RVFcG51d4AnMqDNPkQosd32t2pJ89MZO5zvzn9B6ObGVZJG++uCnODIEw2nGgb+EYH2W5fLUusPFlFs100MQuG4LYrgoVi/JHHvlbrIEWNa7sCXOcewPHULcee1RsmTWzQ3HwWdaF6OB/HWIBFb2GhXxO6GWMjxUqGMFxaZT0o53+2kaew3nC/p5ijtp1jfbIsTOxr4BLhnZekjmdupczv/vs961B2dDstjPwZhnjNUZOQfr78UIB8BzKvH0JM2cbKGpS8H1VAonzm9Nf69gR5qvx0dK7ucMWJJcKWRB0ja+k7uap1HXuH0AX47fhNHhuEj4uBwYqalsHtxF+TLdRUP1+a2ohQRnMiV/rpHnB5jb0Tn7s2/ATW/OfyNlffXVBhps2skrBOqEsLJ7WwpMEeJ7J5pskubl3vTKj7sUUQbSCwUSkJ9Oh8Pt4ehYGRyXGoynXSHlO+DANLiyMM/HQt6XDy0XyPjyOzhFQrW7NP7gK0DG6htaC5nwNOESv2IDqUUeDOmyHPB19zJrzEVQ9hcbqAdq0AA=212FD3x19z9sWBHDJACbC00B75E

#Everytime hit below URL, that generates code as per the following line on Network tab of the inspect window.
https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=http://localhost:8080/td&client_id=TMFGIHQ7NBULNNLAPRMDVSTKTMNVBDUF%40AMER.OAUTHAP

code=E+MejqbKCzpJK+gZEjngIHcfZ0zzm/W0Qf6FlryWSk/py/YMgpdS6KZgVXhyJx/cxMS/56uVNdRGAwtN5x0dEsoNaqrDtkHq1N/K7xsAMa/wsYbakuSu4u8nqW+w1exQobHSCspzkD96wmQvJWUEOzOT8q7QCce76CdSciAjcsysf5zVEqjXD5KYk+QffXtQR7k/StnIwJT73D5d6KSmOxsN7Ty4MJnzUbbUPI1DsqSWDP/V47L9veDQbQyOMMAlXUSBno0EG/blwASZ0NqXOxUva8caGLCUnlvVUvxbyoda9RqO1EDfASXwCv2rq7hTA7Q8ldC5eAi4ak9kwvLJyPiEakeqA69AiWNRm//wo4UDPGFbJr0ByJPrV4YYwAM2xpqsfH6apqHMD3btRGxRj+gPk4VgxBfJynG4/IRZI9XKfYGKfda0oerH69d100MQuG4LYrgoVi/JHHvlt8+oVLLfBrJuIwmqUELf3Ri85Sr7XYoy4rX6kz/dFd7WyaekJE2ETaCPnbu3FUAZDoTl1+JLENG8KGKcnI2pPgV98moxAnKzCNauly1rEWmvzk57+OVOL3+1AuxpMhYsk31d4l6yRLWdnVCXdYk1ulIF6an0EshSAMnNI3lYuaiTyepLYrxLy5UXzfOlcGfh5iv5Snx/B5T/8oHs9HtpDwExYDZFVxndS80fzRBnjsXeQtyUoTSFM92Po2dxgVwPZOmktKSEkryvHeJeImGCXLPt3D6sgd1awORpul+FgnB6Ala5NMLxhigBk+46346fGdnWo5U+V26sj91FBZiY2kuyfm1p84EmWYZytnaGADb49eRPjZOjPWR/ZMaEPC8+5GakNUJ+xO8Z8nAmWjV6LXclW2ANmMmEPNSzcH27arMQLJZJb0kOUeItnpo=212FD3x19z9sWBHDJACbC00B75E

#####################
curl -X POST --header "Content-Type: application/x-www-form-urlencoded" -d "grant_type=authorization_code&refresh_token=&access_type=&code=E%2BMejqbKCzpJK%2BgZEjngIHcfZ0zzm%2FW0Qf6FlryWSk%2Fpy%2FYMgpdS6KZgVXhyJx%2FcxMS%2F56uVNdRGAwtN5x0dEsoNaqrDtkHq1N%2FK7xsAMa%2FwsYbakuSu4u8nqW%2Bw1exQobHSCspzkD96wmQvJWUEOzOT8q7QCce76CdSciAjcsysf5zVEqjXD5KYk%2BQffXtQR7k%2FStnIwJT73D5d6KSmOxsN7Ty4MJnzUbbUPI1DsqSWDP%2FV47L9veDQbQyOMMAlXUSBno0EG%2FblwASZ0NqXOxUva8caGLCUnlvVUvxbyoda9RqO1EDfASXwCv2rq7hTA7Q8ldC5eAi4ak9kwvLJyPiEakeqA69AiWNRm%2F%2Fwo4UDPGFbJr0ByJPrV4YYwAM2xpqsfH6apqHMD3btRGxRj%2BgPk4VgxBfJynG4%2FIRZI9XKfYGKfda0oerH69d100MQuG4LYrgoVi%2FJHHvlt8%2BoVLLfBrJuIwmqUELf3Ri85Sr7XYoy4rX6kz%2FdFd7WyaekJE2ETaCPnbu3FUAZDoTl1%2BJLENG8KGKcnI2pPgV98moxAnKzCNauly1rEWmvzk57%2BOVOL3%2B1AuxpMhYsk31d4l6yRLWdnVCXdYk1ulIF6an0EshSAMnNI3lYuaiTyepLYrxLy5UXzfOlcGfh5iv5Snx%2FB5T%2F8oHs9HtpDwExYDZFVxndS80fzRBnjsXeQtyUoTSFM92Po2dxgVwPZOmktKSEkryvHeJeImGCXLPt3D6sgd1awORpul%2BFgnB6Ala5NMLxhigBk%2B46346fGdnWo5U%2BV26sj91FBZiY2kuyfm1p84EmWYZytnaGADb49eRPjZOjPWR%2FZMaEPC8%2B5GakNUJ%2BxO8Z8nAmWjV6LXclW2ANmMmEPNSzcH27arMQLJZJb0kOUeItnpo%3D212FD3x19z9sWBHDJACbC00B75E&client_id=TMFGIHQ7NBULNNLAPRMDVSTKTMNVBDUF&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Ftd" "https://api.tdameritrade.com/v1/oauth2/token"

grant_type=authorization_code
code=<ABOVE_GENERATED_CODE>
client_id=
redirect_url=

Above will send response back with access token as below

{
    "access_token": "GKVRPt92cpPqheVENhT2ZGgQdx1QJq76EhOqjKN0qViLet6PnGkfp7FFGHHg0Zzz8KDByg2c7LL/4rF+Bq/GGcJUNGe59psIzx1YEWsm4w4qYt06hO6uR5kbsFN4wphY1Sfw6oiHluPNodH1Kmjg60rew0wXcp/pQZd3rum8RAVW2uQb9plbAs0pnt+yL0rP3LV6GHNGfynWJ79fvPokXcXvdcN2eiAeFKkiD/9OpNScQ5xbEVD+S8f8wXxXsVpdN1O28TLlNi+f4RFcDQdmX3ABAFRzvf+Yd1BaLQ4qmpjzjUw8iA6TP/+SS8d9l94jHzW5w+GMpEytlsvMlAZ53lNu7z87naxbNxZk3xTPzm9MLhBOce7PfJiuNlTgUxGuuomzzZyGmWchUCoX/Gyglm68VCrofMcaF7l8j2HQ7qalD9D37fSBUTYMY4zL+s8/Kt9Wk6VFX23h3uf76J0y/7gZRd11+qap+0OxQ2idFOw2IcZpgxorYWn3qYxOVqzFjSjq9d/3rXNv4Trx/svn/4kBlWDlEjpeVWumNSZP1poAnoxey100MQuG4LYrgoVi/JHHvl2KITt5kS/kTwEjccKJKZPBz3hnjU2yOPLcAjdR5qnBHu4ZlJVcyX3JdeiwPAh0dpQHCe1Jgv8Rok8qyzD2oZAc+ShcUJFvVxgABDp71BzNTMhls8Y72VOjo6zrbdZP8FdG8ma2Du/FpEGS2MNkNC3YZEZCWIFuiyJtqH78xA5ohyL0cq85MTr9VAC4vGWGzZWGyjvu3MvsJTsTOcJZfVzx9s28bEgEGdVTCfXHK4JQeWEFe41BShOAuRn0LYeORozNccT6YOwhd9b4RWfPMYUUXMRtQInw3o9NKqDrLlW3mBbij7XBk9QRejExdtswBA4icFt0DzzYatpJwr6IUC/W4923XQH9PBAWushITQSBEKAPY7nYKcM8iSIY1ToE5F/bG1CpAVRhu0CNcEbCyd+LU5cij4pITBLbTNU9SbxCEP50rDYXvU55/DMEP3yGzMRaMgYWLilZ7qhQ5xAKFwVGrSga5QtiBbU1zbzF8fR2dJxIDgOHYWj+69JV0boWvxDGWjZVULNbibb/gV5uW1HjM2n4uHQ8Nw0zv0jth922rrWF9g==212FD3x19z9sWBHDJACbC00B75E",
    "scope": "PlaceTrades AccountAccess MoveMoney",
    "expires_in": 1800,
    "token_type": "Bearer"
}

########################

Sample API call to find fundamentals of a stock

curl -X GET --header "Authorization: Bearer GKVRPt92cpPqheVENhT2ZGgQdx1QJq76EhOqjKN0qViLet6PnGkfp7FFGHHg0Zzz8KDByg2c7LL/4rF+Bq/GGcJUNGe59psIzx1YEWsm4w4qYt06hO6uR5kbsFN4wphY1Sfw6oiHluPNodH1Kmjg60rew0wXcp/pQZd3rum8RAVW2uQb9plbAs0pnt+yL0rP3LV6GHNGfynWJ79fvPokXcXvdcN2eiAeFKkiD/9OpNScQ5xbEVD+S8f8wXxXsVpdN1O28TLlNi+f4RFcDQdmX3ABAFRzvf+Yd1BaLQ4qmpjzjUw8iA6TP/+SS8d9l94jHzW5w+GMpEytlsvMlAZ53lNu7z87naxbNxZk3xTPzm9MLhBOce7PfJiuNlTgUxGuuomzzZyGmWchUCoX/Gyglm68VCrofMcaF7l8j2HQ7qalD9D37fSBUTYMY4zL+s8/Kt9Wk6VFX23h3uf76J0y/7gZRd11+qap+0OxQ2idFOw2IcZpgxorYWn3qYxOVqzFjSjq9d/3rXNv4Trx/svn/4kBlWDlEjpeVWumNSZP1poAnoxey100MQuG4LYrgoVi/JHHvl2KITt5kS/kTwEjccKJKZPBz3hnjU2yOPLcAjdR5qnBHu4ZlJVcyX3JdeiwPAh0dpQHCe1Jgv8Rok8qyzD2oZAc+ShcUJFvVxgABDp71BzNTMhls8Y72VOjo6zrbdZP8FdG8ma2Du/FpEGS2MNkNC3YZEZCWIFuiyJtqH78xA5ohyL0cq85MTr9VAC4vGWGzZWGyjvu3MvsJTsTOcJZfVzx9s28bEgEGdVTCfXHK4JQeWEFe41BShOAuRn0LYeORozNccT6YOwhd9b4RWfPMYUUXMRtQInw3o9NKqDrLlW3mBbij7XBk9QRejExdtswBA4icFt0DzzYatpJwr6IUC/W4923XQH9PBAWushITQSBEKAPY7nYKcM8iSIY1ToE5F/bG1CpAVRhu0CNcEbCyd+LU5cij4pITBLbTNU9SbxCEP50rDYXvU55/DMEP3yGzMRaMgYWLilZ7qhQ5xAKFwVGrSga5QtiBbU1zbzF8fR2dJxIDgOHYWj+69JV0boWvxDGWjZVULNbibb/gV5uW1HjM2n4uHQ8Nw0zv0jth922rrWF9g==212FD3x19z9sWBHDJACbC00B75E" "https://api.tdameritrade.com/v1/instruments?apikey=TMFGIHQ7NBULNNLAPRMDVSTKTMNVBDUF&symbol=AAPL&projection=fundamental"

