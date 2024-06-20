from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from .models import WeatherData

BASE_URL = 'https://api.openweathermap.org/data/2.5/onecall'

class GetWeatherAPIView(APIView):
    
  def get(self, request, *args, **kwargs):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    detailing_type = request.GET.get('detailing_type')

    if not lat or not lon or not detailing_type:
        return Response({"error": "Please click on map above to select location first (lat, lon, and detailing_type are required parameters.)"},
                        status=status.HTTP_400_BAD_REQUEST)
    
    
    time_before_10_minutes = timezone.now() - timezone.timedelta(minutes=10)
    weather_data = WeatherData.objects.filter(lat=lat, lon=lon, detailing_type=detailing_type, timestamp__gte=time_before_10_minutes).order_by('-timestamp').first()
    
    if weather_data:
        return Response(weather_data.data)
    
    exclude_list = ['current', 'minutely', 'hourly', 'daily']

    if detailing_type in exclude_list:
      exclude_list.remove(detailing_type)


    
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': ','.join(exclude_list),
        'appid': settings.OPEN_WEATHER_API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        return Response({"error": "Failed to fetch data from OpenWeatherMap."},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    data = response.json()

    if weather_data:
        weather_data.data = data
        weather_data.timestamp = timezone.now()
        weather_data.save()
    else:
        WeatherData.objects.create(lat=lat, lon=lon, detailing_type=detailing_type, data=data)
    
    return Response(data)

@api_view(['GET'])
def get_weather(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    detailing_type = request.GET.get('detailing_type')

    if not lat or not lon or not detailing_type:
        return Response({"error": "Please click on map above to select location first (lat, lon, and detailing_type are required parameters.)"},
                        status=status.HTTP_400_BAD_REQUEST)
    
    
    time_before_10_minutes = timezone.now() - timezone.timedelta(minutes=10)
    weather_data = WeatherData.objects.filter(lat=lat, lon=lon, detailing_type=detailing_type, timestamp__gte=time_before_10_minutes).order_by('-timestamp').first()
    
    if weather_data:
        return Response(weather_data.data)
    
    exclude_list = ['current', 'minutely', 'hourly', 'daily']

    if detailing_type in exclude_list:
      exclude_list.remove(detailing_type)


    
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': ','.join(exclude_list),
        'appid': settings.OPEN_WEATHER_API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        return Response({"error": "Failed to fetch data from OpenWeatherMap."},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    data = response.json()

    if weather_data:
        weather_data.data = data
        weather_data.timestamp = timezone.now()
        weather_data.save()
    else:
        WeatherData.objects.create(lat=lat, lon=lon, detailing_type=detailing_type, data=data)
    
    return Response(data)
