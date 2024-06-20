# Create your models here.
from django.db import models
from django.utils import timezone

class WeatherData(models.Model):
  lat = models.FloatField()
  lon = models.FloatField()
  detailing_type = models.CharField(max_length=20)
  data = models.JSONField()
  timestamp = models.DateTimeField(default=timezone.now)