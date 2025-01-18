import requests
from datetime import datetime
import smtplib

MY_LAT = -17.838619 # Your latitude
MY_LONG = 31.106882 # Your longitude
MY_EMAIL = "vuyisile.maffles@yahoo.com"
MY_PASSWORD = "tljubydyeqzknzqi"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#   Your position is within +5 or -5 degrees of the ISS position.


def iss_position_overhead():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour


def dark_outside():
    if current_hour > sunset or current_hour < sunrise:
        return True


#   If the ISS is close to my current position
#   and it is currently dark
#   Then send me an email to tell me to look up.
#   BONUS: run the code every 60 seconds.

if iss_position_overhead() and dark_outside():
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: ISS NOTIFICATION!\nTo: {MY_EMAIL}\n From: {MY_EMAIL}\n\n"
                                f"Go Outside! The International Space Station is near you and visible!!")
