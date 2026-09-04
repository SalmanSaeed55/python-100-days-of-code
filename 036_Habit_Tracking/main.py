import requests
import datetime

today = datetime.datetime.now()

TOKEN = "23343js234jsghwghl"
USERNAME = "salman123"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = "https://pixe.la/v1/users/salman123/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_params = {
    "id": GRAPH_ID,
    "name": "Steps Tracker",
    "unit": "steps",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
params = {
    "date": today.strftime("%Y%m%d"), # yyyyMMdd
    "quantity": "3000"
}

response = requests.post(url=pixel_creation_endpoint, json=params, headers=headers)
print(response.text)