from django.shortcuts import render
from django.http import HttpResponse
# from django.urls import reverse
import requests


def get_weather_by_city(request):
    # return HttpResponse(city)
    city = request.GET.get("city")
    if city is not None:
        # city = request.GET.get('city', city)  # Default city if not provided
        # TODO get key from settings
        api_key = 'settings.WEATHER_API_KEY'
        api_url = 'settings.WEATHER_API_UR'

        # response = requests.get(api_url, params={'key': api_key, 'q': city})
        # weather_data = response.json()

    # context = {
    #     'city': city,
    #     'temperature': weather_data['current']['temp_c'],
    #     'condition': weather_data['current']['condition']['text'],
    # }

    # if response.status_code == 200:
    #     data = response.json()
    #     temp = data['main']['temp']
    #     desc = data['weather'][0]['description']
    #     print(f'Temperature: {temp} K')
    #     print(f'Description: {desc}')
    # else:
    #     return HttpResponse('Error fetching weather data')

    return render(request, 'weather/weather.html', {'city': city})
