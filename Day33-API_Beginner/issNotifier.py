############# OVERHEAD NOTIFIER ############
#If ISS is close to my current position 
# and IF it is currently dark
# send me an email telling me to look up
# BONUS - Run the code every 60 seconds 

import smtplib
import keys
import requests
import datetime as dt
import time

def is_iss_overhead():
    ISS_response_code = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(ISS_response_code.status_code)
    ISS_response_code.raise_for_status() #Requests module can raise Exceptions instead of manual input 
    ISS_data = ISS_response_code.json()

    iss_long_data = ISS_data['iss_position']['longitude']
    iss_lat_data = ISS_data['iss_position']['latitude']

    ## CHECK: Is our position within +5 or -5 degrees of the ISS position ##
    if keys.MY_LAT-5 <= iss_lat_data <= keys.MY_LAT+5 and keys.MY_LONG-5 <= iss_long_data <= keys.MY_LONG+5:
        return True


def is_nighttime():
    my_parameters = {
        "lat": keys.MY_LAT,
        "lng": keys.MY_LONG,
        "formatted": 0#,
        #"date": "2022-12-25"
    }
    #date (string): Date in YYYY-MM-DD format.


    response = requests.get("https://api.sunrise-sunset.org/json", params=my_parameters)
    #response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng=-{MY_LONG}")
    response.raise_for_status()
    data = response.json()

    sunrise24 = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset24 = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset24 or time_now <= sunrise24:
        #It's Dark
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_nighttime():
        with smtplib.SMTP("smtp.mail.yahoo.com") as new_connection:
            new_connection.starttls() #Transpor Layer Security 
            new_connection.login(user=keys.SEND_EMAIL, password=keys.PASSWORD)
            new_connection.sendmail(
                from_addr=keys.SEND_EMAIL,
                to_addrs=keys.REC_EMAIL,
                msg="Subject:ISS Look-Up 🛰\n\nThe ISS is above you in the night sky!"
            )