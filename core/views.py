from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
from .forms import DictionaryForm

# def home(request):
#     is_cached = ('geodata' in request.session)

#     if not is_cached:
#         ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
#         params = {'access_key': settings.IPSTACK_API_KEY}
#         response = requests.get('http://api.ipstack.com/103.216.51.117?access_key=c3ae01b20017a4dc59fa423101f5fe05')
#         # response = requests.get('http://api.ipstack.com/%s' % ip_address, params=params)
#         request.session['geodata'] = response.json()

#     geodata = request.session['geodata']

#     return render(request, 'core/home.html', {
#         'ip': geodata.get('ip'),
#         'country': geodata.get('country_name', ''),
#         'latitude': geodata.get('latitude', ''),
#         'longitude': geodata.get('longitude', ''),
#         'api_key': settings.GOOGLE_MAPS_API_KEY,
#         'is_cached': is_cached
#     })
def home(request):
    response = requests.get('http://api.ipstack.com/103.216.51.117?access_key=c3ae01b20017a4dc59fa423101f5fe05')
    geodata = response.json()
    context = {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata.get('latitude', ''),
        'longitude': geodata.get('longitude', ''),
        'api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'core/home.html', context)

def currentLocation(request):
    response = requests.get('http://api.ipstack.com/103.216.51.117?access_key=c3ae01b20017a4dc59fa423101f5fe05')
    geodata = response.json()
    context = {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata.get('latitude', ''),
        'longitude': geodata.get('longitude', ''),
        'api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    response = requests.get('http://api.ipstack.com/103.216.51.117?access_key=c3ae01b20017a4dc59fa423101f5fe05')
    return HttpResponse('<h1>Current Location<h1>')

def goto(request):
    response = requests.get('https://www.openstreetmap.org/directions?engine=fossgis_osrm_bike&route=11.5684%2C104.8912%3B11.5040%2C104.8834#map=14/11.5350/104.9007')
    geodata = response.json()
    return render(request, 'core/home.html', {})

def api(request):
    # response = requests.get('https://routing.openstreetmap.de/routed-bike/route/v1/driving/104.8912,11.5684;104.8834,11.504?overview=false&geometries=polyline&steps=true')
    # getdata = response.json()

    # data = {

    # }
    return render(request, 'core/draw_map.html')


# https://routing.openstreetmap.de/routed-bike/route/v1/driving/104.8912,11.5684;104.8834,11.504?overview=false&geometries=polyline&steps=true

# https://graphhopper.com/api/1/route?vehicle=car&locale=en-US&key=LijBPDQGfu7Iiq80w3HzwB4RUDJbMbhs6BU0dEnn&ch.disable=true&elevation=false&instructions=true&point=11.5684%2C104.8912&point=11.504%2C104.8834

# openstreetmap
# 11.5684, 104.8912    to  11.5040, 104.8834  map 11.5362, 104.8875
# https://www.openstreetmap.org/directions?engine=fossgis_osrm_bike&route=11.5684%2C104.8912%3B11.5040%2C104.8834#map=14/11.5362/104.8875

# google
# 11.5042044,104.8839082 to 11.5737702,104.8932019
# https://www.google.com/maps/dir/11.5684,104.8912/11.5040,104.8834/@11.5362,104.8875,12z/data=!4m2!4m1!3e0
