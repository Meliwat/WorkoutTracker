import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "220"
HEIGHT_CM = "190"
AGE = "20"

APP_ID = "416c122a"
API_KEY = "91a215954121ff73e784ce4ae295ebef"

excersize_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/565ccd2fcabce96fb2a5b7a24848957a/workouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

excersize_configs = {
    "query": input("Enter your workout: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=excersize_endpoint, json=excersize_configs, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for i in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
        
    }

sheet_response = requests.post(url=sheety_endpoint, json=sheet_input)
print(sheet_response.text)