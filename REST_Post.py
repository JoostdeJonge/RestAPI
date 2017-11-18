import requests
import json

data = {"title" : "nog eentje"}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}

url = 'http://localhost:5000/todo/api/v1.0/tasks'

response = requests.post(url, data=data_json, headers=headers)

print(response)