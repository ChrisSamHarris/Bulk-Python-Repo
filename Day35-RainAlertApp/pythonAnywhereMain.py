########## APPLICABLE AS IT IS A FREE ACCOUNT #########
#PAnywhere = Tasks 
#In order to create a scheduled tasks go on PythonAnywhere and then /user/<userName>/tasks_tab
#COMMAND: export <env_key>=<env_value>; python3 pythonAnywhereMain.py

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient ###
import keys
import json
from datetime import datetime


current = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={keys.CITY},{keys.COUNTRY}&appid={keys.API_KEY}")
current_data = current.json()

########## IS IT GOING TO RAIN OVER THE NEXT 12 HOURS? ###########
OWM_Enpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": keys.LAT,
    "lon": keys.LON,
    "appid": keys.API_KEY,
    "exclude": "current,minutely,daily"
}

hourly_weather = requests.get(OWM_Enpoint, params=weather_params)
hourly_weather.raise_for_status()
hourly_weather_data = hourly_weather.json()

with open("12_hour.json", "w") as json_file:
    json.dump(hourly_weather_data, json_file)

print(hourly_weather_data)

time_list = []
indx = 0
it_will_rain = 0
for i in range(0, 12): #Could also slice up to the desired time i.e. indx = :12
    time_utc = hourly_weather_data["hourly"][indx]["dt"]
    time = datetime.utcfromtimestamp(time_utc).strftime('%d-%m-%Y %H:%M')
    if hourly_weather_data["hourly"][indx]["weather"][0]["id"] < 701: #Documentation of the OpenWeatherAPI shows some form of rain if the weather:id is 700 or less
        print(f"It is forecast to rain at {time}")
        time_list.append(datetime.utcfromtimestamp(time_utc).strftime('%H:%M'))
        it_will_rain += 1
    indx += 1

if it_will_rain > 0:
    proxy_client = TwilioHttpClient() ##
    proxy_client.session.proxies = {'https': os.environ['https_proxy']} ##



print(time_list)

########## TWILIO TO SEND SMS INTO TEXT ###########

client = Client(keys.twilio_account_sid, keys.twilio_auth_token, http_client=proxy_client) ##

message = client.messages \
                .create(
                     body=f"It's going to rain today at the following times {time_list}, remember to bring an Umberella.☔️🌧",
                     from_='+12344234055',
                     to='+447936630297'
                 )

print(message.sid)