from django.shortcuts import render
from .tasks import fetch_weather_data
from .models import WeatherData
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to homepage.")

def no_city_provided(request):
    return HttpResponse("Please provide a city name in the URL, e.g., /weather/NewYork/")



def weather_view(request, city):
    fetch_weather_data(city)
    recent_data = WeatherData.objects.filter(city=city).order_by('-timestamp')
    avg_temp = recent_data[0].calculate_average_temperature() if recent_data else None

    context = {
        'city': city,
        'recent_data': recent_data,
        'average_temperature': avg_temp,
        'extreme_alert': "Yes" if recent_data and avg_temp > 35 else "No",  # Example condition
    }
    return render(request, 'weather/weather_view.html', context)

# Create your views here.
