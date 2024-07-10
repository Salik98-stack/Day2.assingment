import pandas as pd
import requests
import json

url = "http://api.open-notify.org/iss-now.json"
records = []
num_records = 100

for i in range(num_records):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        timestamp = data["timestamp"]

        records.append({
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": timestamp
        })
    else:
        print("Failed to retrieve data:", response.status_code)


df = pd.DataFrame(records)
print(df.head())

df.to_csv("iss_location.csv")