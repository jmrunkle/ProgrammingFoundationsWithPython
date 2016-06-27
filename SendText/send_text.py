from twilio.rest import TwilioRestClient

account_sid = "ACbe0c1da2c1998edd5f5e835c6f63d2a1" # Your Account SID from www.twilio.com/console
auth_token  = "c8521631a302d796472b615a791f66e5"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+16197080499",
    from_="+12017208446",
    body="Hello from Python!")

print(message.sid)