############# SUNRISE SUNSET API ############
import keys
import requests
import datetime as dt


today = dt.datetime.now()

parameters = {
    "lat": keys.MY_LAT,
    "lng": keys.MY_LONG,
    "formatted": 0#,
    #"date": "2022-12-25"
}
#date (string): Date in YYYY-MM-DD format.

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng=-{MY_LONG}")
response.raise_for_status()
data = response.json()
sunrise12 = data["results"]["sunrise"] #results given with AM or PM 12 Hour Clock | IF formatted : 1
sunset12 = data["results"]["sunset"]
sunrise24 = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset24 = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise12)
# print(sunset12)

print(sunrise24)
print(sunset24)

print(today.hour)