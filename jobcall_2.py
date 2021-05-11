from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = MessagingResponse('Hey! How you doing? ')
    # Determine the right reply for this message
    print(body)
    #message = client.messages('MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX').fetch()

    #print(message.to)
    return str(resp)
    
if __name__ == "__main__":
    app.run(debug=True)