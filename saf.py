
import base64

import requests
from requests.auth import HTTPBasicAuth

from config import Config


  
consumer_key = Config.consumer_key
consumer_secret = Config.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
  
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
  
access_token_response = r.json()
  


#encode function
#data to encode = business shortcode + lipa na mpesa passkey + formatted_time
def encode(x,y,z):

    message = x+y+z
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')

    return base64_message


def lipa_request():
    access_token = access_token_response["access_token"]
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": Config.BusinessShortCode,
    "Password": encode(Config.BusinessShortCode, Config.lipa_na_mpesa_passkey, Config.Timestamp),
    "Timestamp": Config.Timestamp,
    "TransactionType": Config.TransactionType,
    "Amount": Config.Amount,
    "PartyA": Config.PartyA,
    "PartyB": Config.PartyB,
    "PhoneNumber": Config.PhoneNumber,
    "CallBackURL": Config.CallBackURL,
    "AccountReference": Config.AccountReference,
    "TransactionDesc": Config.TransactionDesc
    }
  
    
    response = requests.post(api_url, json = request, headers=headers)
  
    print (response.text)

lipa_request()




  

  
