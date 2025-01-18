##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt
import os

# 1. Update the birthdays.csv

now = dt.datetime.now()
birth_date = now.day
birth_month = now.month
#   Empty string variable to store the body of the template
birthday_message = ""
birthday_data = pandas.read_csv("birthdays.csv")
# everyone = birthday_data.to_dict(orient="records")

#   Takes every .txt template in 'letter_templates' directory and stores it in a list
birthday_templates = [file for file in os.listdir("letter_templates") if file.endswith(".txt")]

MY_EMAIL = "vuyisile.maffles@yahoo.com"
MY_PASSWORD = "tljubydyeqzknzqi"

for index, row in birthday_data.iterrows():
    random_template = random.choice(birthday_templates)

    # 2. Check if today matches a birthday in the birthdays.csv
    if row["month"] == birth_month and row["day"] == birth_date:
        name = row["name"]
        email = row["email"]

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
    # name from birthdays.csv
        with open(f"letter_templates/{random_template}", "r") as template_file:
            for line in template_file.readlines():
                line = line.replace("[NAME]", f"{name}")
                birthday_message += line

    # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject: BIRTHDAY WISHES!!\nTo: {email}\nFrom: {MY_EMAIL}\n\n{birthday_message}")

        birthday_message = ""
