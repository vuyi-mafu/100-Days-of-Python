import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

MY_WEIGHT = 65
MY_HEIGHT = 165
MY_AGE = 28

date = datetime.now()
current_date = date.strftime("%d/%m/%Y")
current_time = date.strftime("%H:%M:%S")

auth_username = os.environ.get("auth_username")
auth_password = os.environ.get("auth_password")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me about your exercises today: "),
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE,
}

response = requests.post(nutritionix_endpoint, json=parameters, headers=headers)

exercise = response.json()["exercises"]

duration = response.json()["exercises"]
calories = response.json()["exercises"]

basic = HTTPBasicAuth(username=auth_username, password=auth_password)

sheety_endpoint = os.environ.get("sheety_endpoint")

for exercise_index in range(len(exercise)):

    sheety_parameters = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise[exercise_index]["name"].title(),
            "duration": duration[exercise_index]["duration_min"],
            "calories": calories[exercise_index]["nf_calories"],
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_parameters, auth=basic)


