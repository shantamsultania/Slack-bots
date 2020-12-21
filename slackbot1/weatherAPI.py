import requests
import json

api_key = "" # get your access token from Open Weathermap.or and insert it here 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "London"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
x = response.json()

z = x['weather']

if x["cod"] != "404":
    y = x['main']
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    k = x['wind']

    weather_description = z[0]["description"]
    print("wind speed "+str(k["speed"])+"\nTemperature (in kelvin unit) = " +
          str(current_temperature) +
          "\natmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\nhumidity (in percentage) = " +
          str(current_humidiy) +
          "\ndescription = " +
          str(weather_description))

else:
    print(" City Not Found ")
