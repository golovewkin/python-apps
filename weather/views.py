from django.shortcuts import render
import requests
from .forms import CityForm


def get_weather(request):
    form = CityForm(request.GET or None)

    if form.is_valid():
        city = form.cleaned_data['city']
        api_key = 'settings.WEATHER_API_KEY'
        api_url = 'settings.WEATHER_API_URL'

        response = requests.get(api_url, params={'key': api_key, 'q': city})
        weather_data = response.json()

        context = {
            'city': city,
            'temperature': weather_data['current']['temp_c'],
            'condition': weather_data['current']['condition']['text'],
        }
    else:
        context = {'form': form}

    return render(request, '../templates/weather/weather.html', context)
