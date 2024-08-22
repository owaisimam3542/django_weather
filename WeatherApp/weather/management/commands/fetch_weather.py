from django.core.management.base import BaseCommand
from weather.tasks import fetch_weather_data

class Command(BaseCommand):
    help = 'Fetch weather data periodically'

    def handle(self, *args, **kwargs):
        cities = ['City1', 'City2']  # Replace with your city list
        for city in cities:
            fetch_weather_data(city)
            self.stdout.write(self.style.SUCCESS(f"Fetched weather data for {city}"))
