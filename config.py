from datetime import datetime
import base64
def generate_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")



class Config(object):
    BusinessShortCode= "174379"
    Timestamp =  generate_timestamp()
    TransactionType = "CustomerPayBillOnline"#CustomerBuyGoodsOnline/CustomerPayBillOnline
    Amount =  "1"
    PartyA = "254721694125"
    PartyB = "174379" #Business short code
    PhoneNumber = "254721694125"
    CallBackURL   = "https://www.devphase254@heroku.com"
    AccountReference = "SENSUAL MASSAGE"
    TransactionDesc = "Pay for a Massage"

    lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    consumer_key  = "zNwZXrZe0KlQNADGcfWhxlaNugMbyYcI"
    consumer_secret = "jDGWBZidpezpDmWE"
    