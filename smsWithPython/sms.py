from twilio.rest import Client
from decouple import config

account_sid = 'AC6fd86680d5ac022dc94400ed1325b86a'
auth_token = config("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+14104312721',
    to='+17605500674',
    body="Hello from your python program"
)

print(message.sid)
