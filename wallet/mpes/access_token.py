import requests
from requests.auth import HTTPBasicAuth
from wallet.mpes import keys
def generate_access_token():
    #getting the access tocken
    # consumer_key = consumer_key
    consumer_secret_key = keys.consumer_secret_key
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(keys.consumer_key, consumer_secret_key))
    json_response = r.json()
    my_access_token = json_response["access_token"]
    return my_access_token

