from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_weather),
    path('<str:city>', views.get_weather_by_city, name="city"),
]
