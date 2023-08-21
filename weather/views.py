from django.shortcuts import render
import requests


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
            # TODO get key from settings
            api_key = 'settings.WEATHER_API_KEY'
            api_url = 'settings.WEATHER_API_URI'

            response = requests.get(api_url, params={'key': api_key, 'q': city})
            data = response.json()
            if response.status_code == 200:
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
            else:
                raise Exception(data)
        except Exception as error:
            context['error'] = error

    return render(request, 'weather/weather.html', context)
