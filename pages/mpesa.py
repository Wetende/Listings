from datetime import datetime
import base64
import json
import pprint

from .credentials import lnm_passkey, bs_shortcode, consumer_key, consumer_secrete, acess_token_url

import requests
from requests.auth import HTTPBasicAuth

def format_time():
    unformated_datetime=datetime.now()
    formated_datetime = unformated_datetime.strftime("%Y%m%d%H%M%S") #Formats the datetime i a format the safaricom expects
    return formated_datetime

def decode_password():
    pass_to_be_encoded = bs_shortcode + lnm_passkey + format_time() # The password exected is a combination of shortcode, the passkey, and the formated time
    #Encoding the password
    pass_encoded = base64.b64encode(pass_to_be_encoded.encode()) 
    #Decoding the password
    pass_decoded = pass_encoded.decode('utf_8') 
    return pass_decoded
 
def generate_access_token():
    response = requests.get(acess_token_url, auth=HTTPBasicAuth(consumer_key,consumer_secrete))    
    res_json = response.json()
    #Filtering out the expiry date that is returned together with the access token as a response 
    filtered_access_token = res_json['access_token'] 
    return filtered_access_token
    
def initiate_stk(phone, amount):
    access_token = generate_access_token()
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {"Authorization": "Bearer %s" %access_token }


    request = {    
        "BusinessShortCode":bs_shortcode,    
        "Password":decode_password(),    
        "Timestamp":format_time(),    
        "TransactionType": "CustomerPayBillOnline",    
        "Amount":f"{amount}",    
        "PartyA":f"{phone}",    
        "PartyB":bs_shortcode,    
        "PhoneNumber":f"{phone}",    
        "CallBackURL":"https://essaybees.com/home",    
        "AccountReference":"Wetende Listings",    
        "TransactionDesc":"Pay library penalties"
    }

    response = requests.post(api_url, json=request, headers=headers) #The response can either be a succesful transaction or a failed transaction 
    string_response = response.text
    data_object = json.loads(string_response)
     
    merchant_request_id = data_object["MerchantRequestID"]
    checkout_request_id = data_object["CheckoutRequestID"]
    response_code = data_object["ResponseCode"]
    response_description = data_object["ResponseDescription"]
    customer_message = data_object["CustomerMessage"]

    data = {
        "MerchantRequestID": merchant_request_id,
        "CheckoutRequestID": checkout_request_id,
        "ResponseCode": response_code,
        "ResponseDescription": response_description,
        "CustomerMessage": customer_message,
    } 

    pprint.pprint(data)
