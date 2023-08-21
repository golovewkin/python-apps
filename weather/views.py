from django.shortcuts import render
from django.http import HttpResponse
import requests


def get_weather_by_city(request):
    city = request.GET.get("city")[0]
    context = {
        'city': city,
        'error': '',
        # 'temperature': weather_data['current']['temp_c'],
        # 'condition': weather_data['current']['condition']['text'],
    }

    if context['city'] is not None:
        try:
            # TODO get key from settings
            api_key = 'settings.WEATHER_API_KEY'
            api_url = 'settings.WEATHER_API_URI'

            response = requests.get(api_url, params={'key': api_key, 'q': city})
            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                print(f'Temperature: {temp} K')
                print(f'Description: {desc}')
            else:
                raise Exception("Sorry, request data error")
        except Exception as error:
            context['error'] = error

    return render(request, 'weather/weather.html', context)
