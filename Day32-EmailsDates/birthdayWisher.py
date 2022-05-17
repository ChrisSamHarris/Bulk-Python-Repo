#Task = Automate sending someone a birthday email - Birthdays should be provided in csv: name, email, year, month, day
#Reference letters provided via templates 
import smtplib
import datetime as dt
import keys
import random
import pandas

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./birthday_meta/birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()} #Pandas iterrows:

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"./birthday_meta/letter{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(keys.SEND_EMAIL, keys.PASSWORD)
        connection.sendmail(
            from_addr=keys.SEND_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
            )


####### PythonAnywhere #########

#Use this service to host the code on the cloud, saves running the code everyday 
#Upload code to website 
#Python3 birthdayWisher.py 
#Auth error = unlock captcha
#dashboard > Tasks > Schedule a task using the run "python3 birthdayWisher.py" 
#Command will run at the set time 