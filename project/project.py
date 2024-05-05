import random
import pyodbc
import requests

response = requests.get('https://api.covid19tracker.ca/summary')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")