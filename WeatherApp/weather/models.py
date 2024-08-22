from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    weather_condition = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.timestamp}"

    def calculate_average_temperature(self):
        recent_data = WeatherData.objects.filter(city=self.city).order_by('-timestamp')[:24]
        total_temp = sum([data.temperature for data in recent_data])
        return total_temp / len(recent_data)

# Create your models here.
