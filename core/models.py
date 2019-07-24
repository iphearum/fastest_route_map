from django.db import models

# Create your models here.
class currentLocation(models.Model):
    # ip_address = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)