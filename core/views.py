from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from urllib.request import urlopen
import requests,json
# from .forms import DictionaryForm

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


# view_request
# view page request
def ViewSendRequest(request):
    return render(request,'core/send_request.html')
# show location when get the api
def get_location(request): 
    return render(request, 'core/getDirection.html')
def success_drawing(request): 
    return render(request, 'core/success_drawing.html')



# get_request
# home page
def index(request):
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

# view current location
def current_location(request):
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

# send request to get direction api
def send_request(request):
    if request.method == "POST":
        startpoint = request.POST.get("startpoint", None)
        endpoint = request.POST.get("endpoint", None)
        context = {
            'startpoint':blah(startpoint),
            'endpoint':blah(ndpoint)
        }
        return render(request, 'core/get_request.html', {'result': context})
    return render(request, 'core/get_request.html', {})
    # response = requests.get('https://www.openstreetmap.org/directions?engine=fossgis_osrm_bike&route=11.5684%2C104.8912%3B11.5040%2C104.8834#map=14/11.5350/104.9007')
    # geodata = response.json()
    # return render(request, 'core/home.html', {})

 #get api after send request
def request_to_api(request):
    request_from = '104.8834,11.504'    # lng, lat
    request_end = '104.8834,11.504'  # lng, lat
    response = requests.get('https://routing.openstreetmap.de/routed-bike/route/v1/driving/'+request_from+';'+request_end+'?overview=false&geometries=polyline&steps=true')
    return render(request, 'core/request_api.html')

#just test draw map
def test_api(request):
    request_from = '104.8834,11.504'    # lng, lat
    request_end = '104.88406,11.50503'  # lng, lat
    # response = requests.get('https://routing.openstreetmap.de/routed-bike/route/v1/driving/'+request_from+';'+request_end+'?overview=false&geometries=polyline&steps=true')
    response = requests.get("http://localhost/py/data/general.json")
    json_data = response.json()
    steps = json_data['routes'][0]['legs'][0]['steps']
    new_data = []
    for step in steps:
        intersections = step['intersections']
        for intersection in intersections:
            locations = intersection['location']
            for location in locations:
                lat=location
                for location in locations:
                    if location != lat:
                        lng = location
            new_data.append('{lat:'+str(lat)+',lng:'+str(lng)+'}')
        maneuver = step['maneuver']
    a = '['
    fullStr = ','.join(new_data) # convert list to string
    b = ']'
    new_data = a+fullStr+b #new data is a string
    # please convert string to json data by using javascript <<json.parse(new_data)>>
    # print(new_data)
    context={
        'request_from':request_from,
        'request_end':request_end,
        'map':new_data
    }
    return render(request, 'core/success_drawing.html',context)


# Link = https://www.openstreetmap.org/directions?engine=fossgis_osrm_bike&route=11.5684%2C104.8912%3B11.5040%2C104.8834#map=14/11.5362/104.8875
# API 1 = https://routing.openstreetmap.de/routed-bike/route/v1/driving/104.8912,11.5684;104.8834,11.504?overview=false&geometries=polyline&steps=true