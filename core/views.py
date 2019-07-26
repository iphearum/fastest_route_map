from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from urllib.request import urlopen
import requests,json
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

 #get api after send request
def request_to_api(request):
    request_from = '104.8834,11.504'    # lng, lat
    request_end = '104.8912,11.5684'  # lng, lat
    response = requests.get('https://routing.openstreetmap.de/routed-bike/route/v1/driving/'+request_from+';'+request_end+'?overview=false&geometries=polyline&steps=true')
    return render(request, 'core/request_api.html')

#just test draw map
def test_api(request):
    request_from = '104.8834,11.504'    # lng, lat
    request_end = '104.8912,11.5684'  # lng, lat
    response = requests.get('https://routing.openstreetmap.de/routed-bike/route/v1/driving/'+request_from+';'+request_end+'?overview=false&geometries=polyline&steps=true')
    # response = requests.get("http://localhost/py/data/general.json")
    json_data = response.json()
    steps = json_data['routes'][0]['legs'][0]['steps']
    waypoints = json_data['waypoints']
    # define step routes
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
    fullStr = ','.join(new_data) # convert list to string
    new_data = fullStr
    # print(new_data)

    #define waypoint
    way_route = []
    for waypoint in waypoints:
        locations = waypoint['location']
        for location in locations:
            lat=location
            for location in locations:
                if location != lat:
                    lng = location
            way_route.append('{lat:'+str(lat)+',lng:'+str(lng)+'}')
    new_way_route = ','.join(way_route) # convert list to string
    way_route = new_way_route
    print(way_route)

    # offer data
    context={
        'map':new_data
    }
    return render(request, 'core/success_drawing.html',context)

# Link = https://www.openstreetmap.org/directions?engine=fossgis_osrm_bike&route=11.5684%2C104.8912%3B11.5040%2C104.8834#map=14/11.5362/104.8875
# API 1 = https://routing.openstreetmap.de/routed-bike/route/v1/driving/104.8912,11.5684;104.8834,11.504?overview=false&geometries=polyline&steps=true
