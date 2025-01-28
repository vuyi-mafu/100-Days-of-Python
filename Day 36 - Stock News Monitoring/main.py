import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#   Parameters for stock api
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "5P7HJUX5D6RBDRRL",
}

#   Parameters for news api
news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": "7c8adeafd3534e75b1c10b129295bb09",
}

#   Parameters for twilio api
account_sid = 'ACbe5b794bb9a24bc66d4c8fb472e75126'
auth_token = 'ee883cc8d85374a11403adc3ceadf10e'
client = Client(account_sid, auth_token)

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url='https://www.alphavantage.co/query', params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
# print(stock_data['Time Series (Daily)'])

past_two_days_data_dict = {}
past_two_days_data_list = []
latest_news_list = []

# This loop gets the first two entries of the dictionary
for i, (key, value) in enumerate(stock_data['Time Series (Daily)'].items()):
    if i == 2:
        break
    past_two_days_data_list.append(key)
    past_two_days_data_dict[key] = value

stock_price_change = (float(past_two_days_data_dict[past_two_days_data_list[0]]["4. close"]) -
                      float(past_two_days_data_dict[past_two_days_data_list[1]]["4. close"]))

stock_price_change_percentage = (stock_price_change / float(past_two_days_data_dict[past_two_days_data_list[0]]
                                                            ["4. close"])) * 100
# print(stock_price_change_percentage)
print(past_two_days_data_dict)
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if stock_price_change_percentage <= -2 or stock_price_change_percentage >= 2:

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()
    # print(news_data["articles"])

    for item in range(3):
        latest_news_list.append(news_data["articles"][item])

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

        if stock_price_change_percentage < 0:
            title = f"{STOCK}: 🔻{round(abs(stock_price_change_percentage))}%"
        else:
            title = f"{STOCK}: 🔺{round(abs(stock_price_change_percentage))}%"
        headline = f"Headline: {news_data["articles"][item]["title"]}"
        description = f"Brief: {news_data["articles"][item]["description"]}"

        message = client.messages.create(
            body=f'{title}\n\n{headline}\n\n{description}',
            from_='+15802894065',
            to='+xxxxxxxxxxxx'
        )

        print(message.status)
