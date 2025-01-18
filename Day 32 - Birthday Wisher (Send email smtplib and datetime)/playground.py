import smtplib
import datetime as dt
import random

quotes_list = []
now = dt.datetime.now()

with open("quotes.txt") as datafile:
    #   Takes every line and appends it to a list (quotes_list)
    #   or use quotes_list = datafile.readlines()
    for quote in datafile:
        quotes_list.append(quote)

random_quote = random.choice(quotes_list)

my_email = "vuyisile.maffles@yahoo.com"
password = "tljubydyeqzknzqi"

if now.weekday() == 1:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="vuyimaffles@gmail.com",
                            msg=f"Subject: MOTIVATIONAL QUOTATION\nFrom: {my_email}\n"
                                f"To: vuyimaffles@gmail.com\n\n{random_quote}")


