from datetime import datetime
import base64
def generate_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")



class Config(object):
    BusinessShortCode= "888880"
    Timestamp =  generate_timestamp()
    TransactionType = "CustomerPayBillOnline"
    Amount =  "1"
    PartyA = "254721694125"
    PartyB = " " #Business short code
    PhoneNumber = "254721694125"
    CallBackURL   = "https://www.devphase254@heroku.com"
    AccountReference = "25081419"
    TransactionDesc = "Pay for a Massage"

    lipa_na_mpesa_passkey = ""
    consumer_key  = "zNwZXrZe0KlQNADGcfWhxlaNugMbyYcI"
    consumer_secret = "jDGWBZidpezpDmWE"
    