#import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC2bbdf1ec40ef59464553bdfac86c5201'
auth_token = 'fefeb7f5fa084f3243bccd2007ce2f1f'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+19739794949',
                        from_='+16467988343'
                    )

print(call.sid)