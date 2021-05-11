from twilio.rest import Client

#This is for sending message 

account_sid = 'AC2bbdf1ec40ef59464553bdfac86c5201'
auth_token = 'fefeb7f5fa084f3243bccd2007ce2f1f'
client = Client(account_sid, auth_token)

client.messages.create(
  to="+15512920514",
  from_="+16467988343",
  body="An employer is interested in you! Here is their information. Name: John Smith, Location: 73232, Phone Number: 2343343443, Needs: Cook on weekdays. "
)