from django.shortcuts import render
import requests
from local_settings import API_KEY


def get_weather_by_city(request):
    city = request.GET.get("city")
    context = {
        'city': city,
        'error': '',
        'temperature': '',
        'condition': '',
    }

    if context['city'] is not None:
        try:
            api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

            response = requests.get(api_url, params={'key': API_KEY, 'q': city})
            data = response.json()
            if response.status_code == 200:
                context['temp'] = round((data['main']['temp'] - 32) * 5 / 9)
            else:
                raise Exception(data)
        except Exception as error:
            context['error'] = error

    return render(request, 'weather/weather.html', context)
