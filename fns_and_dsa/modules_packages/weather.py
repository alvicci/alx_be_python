import requests
from config import API_KEY

response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q=osun&appid={API_KEY}")

if (response.status_code == 200):
    
    data = response.json()
    lat = data[0]['lat']
    lon = data[0]['lon']

    weather_response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}")

    if (weather_response.status_code == 200):
        data = weather_response.json()

        current = data["current"]
        current_weather = current["weather"][0]["description"]
        current_temp = current["temp"]

        print("Current Weather:")
        print(f"Temperature: {current_temp}K")
        print(f"Description: {current_weather}")
        # print(data)