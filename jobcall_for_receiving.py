import os
from twilio.rest import Client

#Give your account Id, SID and message ID to see the body of the message 
account_sid = 'AC2bbdf1ec40ef59464553bdfac86c5201'
auth_token = 'fefeb7f5fa084f3243bccd2007ce2f1f'
client = Client(account_sid, auth_token)

message = client.messages('SM9335666f6eb500614c036a117303231f').fetch()

print(message.body)