
import requests
import datetime
import base64

from requests.auth import HTTPBasicAuth
from transaction.models import LNMOnline

from wallet.mpes  import access_token 

from wallet.mpes import keys

def generate_passoword():
    #creating password
    data_to_encode = keys.businessshortCode + keys.lipa_na_mpesa_pass_key + generate_timestamp()
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode('utf8')
    return decoded_password

def generate_timestamp():
    unformated_time = datetime.datetime.now()
    formated_time = unformated_time.strftime("%Y%m%d%H%M%S")
    return formated_time

                                                                                                                                    
def lipa_na_mpesa(phone_number,ammount):
    access_tokens = access_token.generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": f"Bearer {access_tokens}" ,"Content-Type": "application/json" }
    request = {
                "BusinessShortCode": keys.businessshortCode,
                "Password": generate_passoword(),
                "Timestamp": generate_timestamp(), # timestamp format: 20190317202903 yyyyMMhhmmss 
                "TransactionType": "CustomerPayBillOnline",
                "Amount": ammount,
                "PartyA": keys.phone_number,
                "PartyB": keys.businessshortCode,
                "PhoneNumber": phone_number,
                "CallBackURL": "https://tranquil-stream-15304.herokuapp.com/mpesa_callback",
                "AccountReference": "PTC Manager",
                "TransactionDesc": "Sending money to ptc Account"
            }
    response = requests.post(api_url,json=request,headers=headers)

lipa_na_mpesa(phone_number="254717713943",ammount="1")
lnm = LNMOnline.objects.all()
for l in lnm:
    print(l.Amount)


