# 🌟 Mini Project: Weather App (weather_app.py)
# You’ll build a simple weather-fetching app using the Open-Meteo API (no API key required).

# API Endpoint (GET):https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true
# This returns weather for Lagos, Nigeria

# 🧩 What to Do in weather_app.py:
# 1. Make a GET request to the above URL
# 2. Extract and print:
# - Temperature
# - Wind speed
# - Time of the weather update
# 3. Add error handling (e.g., if the server is down)
import requests

try:
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true")
    response.raise_for_status()
    
except requests.exceptions.HTTPError as http_err:
    print(f"Http error occured: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error: {conn_err}")
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
else:
    data = response.json()
    print(f"Temperature : {data["current_weather"]["temperature"]}\nWind speed: {data["current_weather"]["windspeed"]}\nTime of the weather update: {data["current_weather"]["time"]}")