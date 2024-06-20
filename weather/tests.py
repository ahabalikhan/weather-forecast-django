from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import WeatherData

class WeatherAPITestCase(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.url = reverse('get_weather')
    self.lat = '33.441792'
    self.lon = '-94.037689'
    self.detailing_type = 'current'

  def test_get_weather(self):
    response = self.client.get(self.url, {'lat': self.lat, 'lon': self.lon, 'detailing_type': self.detailing_type})
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_missing_parameters(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
