from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
#run_with_ngrok(app)
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a text message
    msg = resp.message("The Robots are coming! Head for the hills!")
    # Add a picture message
    msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)