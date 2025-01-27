import requests
from twilio.rest import Client

api_key = "6d5f31da97a17dcdf1ee24c94b55d38a"
account_sid = "ACbe5b794bb9a24bc66d4c8fb472e75126"
auth_token = "377be813d96c097ca2e390b586c7bc06"

parameters = {
    "lat": -17.825167,
    "lon": 31.033510,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

rain_list = []

for item in range(4):
    if weather_data["list"][item]['weather'][0]["id"] < 700:
        # print("Bring an Umbrella.")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="It's going to rain today. Remember to bring an Umbrella.",
            from_='+15802894065',
            to='+263777122948'
        )
        print(message.status)
        break
