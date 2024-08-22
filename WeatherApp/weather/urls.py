from django.urls import path
from . import views

urlpatterns = [
    path('', views.no_city_provided),
    path('<str:city>/', views.weather_view, name='weather_view'),
]
