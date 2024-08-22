import requests
from .models import WeatherData


def fetch_weather_data(city):
    api_key = "a92a39693a3d4119b7b130555242108"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = WeatherData(
            city=city,
            temperature=data['current']['temp_c'],
            humidity=data['current']['humidity'],
            wind_speed=data['current']['wind_kph'],
            weather_condition=data['current']['condition']['text'],
            # Add more fields as needed
        )
        weather_data.save()
    else:
        # Handle errors
        print("Failed to fetch data:", data)
