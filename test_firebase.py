import requests

FIREBASE_URL = "https://greencrest-dashboard-default-rtdb.firebaseio.com/data.json"

data = {
    "temperature": 30,
    "humidity": 65,
    "gas": 120,
    "status": "testing"
}

response = requests.put(FIREBASE_URL, json=data)

print(response.text)