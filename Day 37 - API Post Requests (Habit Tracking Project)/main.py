import requests
from datetime import datetime, date

TOKEN = "jrwoij34otjoer09erg"
USERNAME = "vuyimafu"
GRAPH_ID = "new-graph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "new-graph",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()
yesterday = date(2025, 1, 29)
yesterday = yesterday.strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

pixel_params = {
    "quantity": "5.55",
}

# response = requests.put(pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

response = requests.delete(pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

