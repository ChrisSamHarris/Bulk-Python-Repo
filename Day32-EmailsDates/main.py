#Plan = Automated birthday email 
#SMTP - Simple Mail Transfer Protocol 
#Required to allow less secure apps: Yahoo > Account > info > Security > login > Generate app password (enter this in keys.PASSWORD)
import smtplib
import datetime as dt
import keys
import random

########## EMAIL ##########
#Gmail: smtp.gmail.com
#Yahoo: smtp.mail.yahoo.com

with smtplib.SMTP("smtp.mail.yahoo.com") as new_connection:
    new_connection.starttls() #Transpor Layer Security 
    new_connection.login(user=keys.SEND_EMAIL, password=keys.PASSWORD)
    new_connection.sendmail(
        from_addr=keys.SEND_EMAIL,
        to_addrs=keys.REC_EMAIL,
        msg="Subject:Test-Hello\n\nThis is TEST EMAIL"
    )


#new_connection.close() - no longer required as the connection will automatically close using the WITH

########## DATETIME ##########

now = dt.datetime.now()
year = now.year

print(year)
print(type(year))

DOB = dt.datetime(year=1995, month=8, day=19, hour=6)
print(DOB)

############ MONDAY MOTIVATIONAL QUOTE ##########
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com") as quote_connection:
        quote_connection.starttls() #secure the connection
        quote_connection.login(user=keys.SEND_EMAIL, password=keys.PASSWORD) #remember yahoo - app password
        quote_connection.sendmail(
            from_addr=keys.SEND_EMAIL,
            to_addrs=keys.REC_EMAIL,
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )
