import requests
import json
import pandas

url = 'http://localhost:5000/todo/api/v1.0/tasks'
response = requests.get(url).json()
print (response)