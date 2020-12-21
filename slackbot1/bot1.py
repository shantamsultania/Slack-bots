import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slackbot1 import tokens as t

# event handling example

# tokens
Access_Token = t.getaccesstoken()
Event_Token = t.getEventToken()

# making a flask connection
app = Flask(__name__)

# slack event api connection
slack_adapter = SlackEventAdapter(Event_Token, "/slack/event", app)

# slack Bot connection
client = slack.WebClient(token=Access_Token)


# get the payload from the user
@slack_adapter.on("message")
def message(payload):
    print(payload)
    print(payload['team_id'])


if __name__ == "__main__":
    app.run()
