from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

def get_weather(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.OPENWEATHER_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    return JsonResponse(data)

