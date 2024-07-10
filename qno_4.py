import json
import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("JSON response:")
    print(json.dumps(data, indent=4))
else:
    print("Failed to retrieve data:", response.status_code)