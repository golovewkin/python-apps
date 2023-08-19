from django.shortcuts import render
from django.http import HttpResponse
import requests


def get_weather(request):
    return HttpResponse('hi')
    city = request.GET.get('city', 'New York')  # Default city if not provided
    api_key = 'settings.WEATHER_API_KEY'
    api_url = 'settings.WEATHER_API_UR'

    # response = requests.get(api_url, params={'key': api_key, 'q': city})
    # weather_data = response.json()

    # context = {
    #     'city': city,
    #     'temperature': weather_data['current']['temp_c'],
    #     'condition': weather_data['current']['condition']['text'],
    # }

    return render(request, 'weather/weather.html', {})
