import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

# OpenWeatherMap API
lat="40.7826"
lon="73.9656"

# 5 day
parameters = {
    "lat": lat,
    "lon": lon,
    "cnt": 4,
    "appid": os.getenv('OWM_API_KEY'),
}

open_weather_map_url = "https://api.openweathermap.org/data/2.5/forecast"

# get weather data
response = requests.get(url=open_weather_map_url, params = parameters)
response.raise_for_status()
weather_data = response.json()

will_need_umbrella = False
for forecast in weather_data['list']:
    if int(forecast['weather'][0]['id']) < 700:
        will_need_umbrella = True


# if it will rain, send a text message (Twilio) as an umbrella reminder
if will_need_umbrella:
    client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    message = client.messages.create(
        body="You will need an umbrella today, it's going to be wet! ☔️",
        from_=os.getenv('TWILIO_NUMBER'),
        to=os.getenv('TARGET_NUMBER'),
    )
    print(message.status)
