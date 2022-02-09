# SENDING EMAILS USING (smtplib) & MANAGING DATES

import smtplib
from datetime import datetime
import datetime as dt
import pandas
import random

# my_mail = "juliusayoola5@gmail.com" with smtplib.SMTP("smtp.gmail.com") as connection: connection.starttls()
# connection.login(user=my_mail , password="#password_here") connection.sendmail(from_addrs= my_mail,
# to_addrs="juliusayoola5@yahoo.com", msg="Subject:Hello Phensic\n\n This is the body of my email") connection.close()


# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday() 
# print(day_of_week)

# date_of_birth = dt.datetime(year=2003, month=10, day=16, hour=3)

# print(date_of_birth)


# EXERCISE 1

MY_EMAIL = "juliusayoola5@yahoo.com"
MY_PASSWORD = "3c7hL#Uyxn~-zYu"

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     with open ("quotes.txt") as quote:
#         quote.readlines()
#         random.choice(quote)
#     print(quote)

# with smtplib.SMTP("smtp.yahoo.com") as connection: 
#     connection.starttls()
#     connection.login(MY_EMAIL, MY_PASSWORD)
#     connection.sendmail (from_addrs=MY_EMAIL, to_addrs= MY_EMAIL, msg=f"Subject: Monday Moltivation\n\n {quote}")


# AUTOMATIC BIRTHDAY WISHING EXERCISE

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {data_row["month"]: data_row["day"] in data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.choice(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addrs=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:HAPPY BIRTHDAY\n\n{contents}")

        # THIS FILE REQUIRES THE DAY 32 COURSE RESOURCES TO COMPLETE
# FINITE
