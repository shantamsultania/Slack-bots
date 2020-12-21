import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from slackbot1 import tokens as t

# Emotional sentiments analyser bot

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


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        return "Negative Sentiment"
    elif score['neg'] < score['pos']:
        return "Positive Sentiment"
    else:
        return "Neutral Sentiment"


# get the payload from the user
@slack_adapter.on("message")
def message(payload):
    event = payload.get('event', {})
    user_id = event.get('user')
    data = event.get('text')
    channel_id = event.get('channel')
    if user_id != Bot_id:
        client.chat_postMessage(channel=channel_id, text=sentiment_analyse(data))
    else:
        print("empty data received ")


if __name__ == "__main__":
    app.run()
