from django.db import models
from django.shortcuts import render
import requests

# Create your models here.
class input(models.Model):
    # ip_address = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)

class Define(models.Model):
    longitud = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    # def __init__(self, start_point, end_point):
    #     self.start_point = start_point
    #     self.end_point = end_point

    def index(self):
        response = requests.get('http://api.ipstack.com/103.216.51.117?access_key=c3ae01b20017a4dc59fa423101f5fe05')
        geodata = response.json()
        context = {
            'ip': geodata['ip'],
            'country': geodata['country_name'],
            'latitude': geodata.get('latitude', ''),
            'longitude': geodata.get('longitude', ''),
        }
        return render(self, 'core/home.html', context)

    def define(self):
        # code
        context={
            'start':self.start_point,
            'end':self.end_point
        }
        return render(self,'core/index.html',context)
