import requests
import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slackbot1 import tokens as t

# get weather BOT

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


def get_weather_details(data):
    api_key = "" # insert Weather APi key here
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = data
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x['main']
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        k = x['wind']
        weather_description = z[0]["description"]
        return ("wind speed " + str(k["speed"]) + "\nTemperature (in kelvin unit) = " +
                str(current_temperature) +
                "\natmospheric pressure (in hPa unit) = " +
                str(current_pressure) +
                "\nhumidity (in percentage) = " +
                str(current_humidiy) +
                "\ndescription = " +
                str(weather_description))

    else:
        return " City Not Found "


# get the payload from the user
@slack_adapter.on("message")
def message(payload):
    event = payload.get('event', {})
    user_id = event.get('user')
    data = event.get('text')
    channel_id = event.get('channel')
    if user_id != Bot_id:
        client.chat_postMessage(channel=channel_id, text=get_weather_details(data))
    else:
        print("empty data received ")


if __name__ == "__main__":
    app.run()
