import requests
from datetime import datetime

APP_ID = "261daf9c"
API_KEY = "ce1d77b0e5bbb48a323df71873bfc9f9"

query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    'x-remote-user-id': '0'
}

parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 50,
    "height_cm": 150,
    "age": 15
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/98152391fda9a6aedfdb74a9d7195ad0/myWorkouts/workouts"

shetty_header = {
    "Authorization": "Bearer ilivemylifewithnoregrets"
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
print(response.json()['exercises'])
result = response.json()['exercises']

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=shetty_header)

    print(sheet_response.text)
