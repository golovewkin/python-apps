from django.shortcuts import render
from django.http import HttpResponse
import requests


def get_weather_by_city(request):
    # return HttpResponse(city)
    city = request.GET.get("city")
    if city is not None:
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
                raise Exception("Sorry, something went wrong, can not get the data")
        except:
            print("An exception occurred")

    context = {
        'city': city,
        # 'temperature': weather_data['current']['temp_c'],
        # 'condition': weather_data['current']['condition']['text'],
    }

    return render(request, 'weather/weather.html', {'city': context})
