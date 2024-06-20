from django.urls import path
from . import views

urlpatterns = [
  path('', views.GetWeatherAPIView.as_view(), name='get_weather')
]