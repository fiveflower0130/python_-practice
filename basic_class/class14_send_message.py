# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client
# from dotenv import load_dotenv
from dotenv import dotenv_values
# load_dotenv()  # take environment variables from .env.

config = dotenv_values(".env")
# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
# twilioo phone number  +18588791532 +1=American number = 8588791532
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = config['TWILIO_ACCOUNT_SID']
auth_token = config['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

numbers_to_message = ['+886919171862']

for number in numbers_to_message:
    message = client.api.account.messages.create(
        # message = client.messages.create(
        to=number,
        from_=config['TWILIO_PHONE_NUMBER'],
        body="This is python send message test. 您好這是python寄簡訊測試程式")
    print(message)
