from twilio.rest import Client

# Please make a seperate file with your Twilio Account information
client = Client("{your account_sid here}", "{your auth_token here}")

class Sms():
    """Twilio sends prank SMS"""

    def __init__(self, sms_title, sms_text):
        self.title = sms_title
        self.text = sms_text

    def send_sms(self, phone_number):
        message = client.messages.create(to="+1"+str(phone_number), from_="+15053693225",body=self.text)
        print("You sent message " + message.sid)
