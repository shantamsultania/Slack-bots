import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slackbot1 import tokens as t

# Re send the message

# tokens
Access_Token = t.getaccesstoken()
Event_Token = t.getEventToken()

# making a flask connection
app = Flask(__name__)

# slack event api connection
slack_adapter = SlackEventAdapter(Event_Token, "/slack/event", app)

# slack Bot connection
client = slack.WebClient(token=Access_Token)

Bot_id = client.api_call('auth.test')['user_id']


def checker(data):
    list1 = ['hi', 'hello']
    list2 = ['bye', 'goodbye']
    d = data.split(" ")
    for i in d:
        for j in list1:
            if j == i:
                return "hello this is test app"
        for k in list2:
            if k == i:
                return "bye nice to see you all "

    return "not found"


# get the payload from the user
@slack_adapter.on("message")
def message(payload):
    event = payload.get('event', {})
    user_id = event.get('user')
    data = event.get('text')
    channel_id = event.get('channel')
    if user_id != Bot_id:
        client.chat_postMessage(channel=channel_id, text=checker(data))
    else:
        print("empty data received ")


if __name__ == "__main__":
    app.run()
