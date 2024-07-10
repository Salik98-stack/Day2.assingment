# import neccessary libraries
import requests
import json

# url to get the data
url = "http://api.open-notify.org/iss-now.json"

# get response from the url
response = requests.get(url)

if response.status_code == 200:
    # convert the response to json
    data = response.json()

    # get latitude and longitude from the json data
    latitude = data["iss_position"]["latitude"]
    longtitude = data["iss_position"]["longitude"]
    timestamp = data["timestamp"] 

    # print the data
    print("Latitude:", latitude)
    print("Longitude:", longtitude)
    print("Timestamp:", timestamp)

else:
    print("Failed to retrieve data:", response.status_code)