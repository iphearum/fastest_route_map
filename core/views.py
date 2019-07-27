from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from urllib.request import urlopen
import requests,json

# view_request
# view page request
class Route:
    def ViewSendRequest(request):
        return render(request,'core/send_request.html')
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
    response.close()
    json_data = response.json()
    steps = json_data['routes'][0]['legs'][0]['steps']
    waypoints = json_data['waypoints']
    # define step routes
    start_point = json_data['waypoints'][0]
    lat_s = start_point['location'][0]
    lng_s = start_point['location'][1]
    end_point = json_data['waypoints'][1]
    lat_e = end_point['location'][0]
    lng_e = end_point['location'][1]
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
    fullStr = ','.join(new_data) # convert list to string
    new_data = fullStr
    # print(new_data)

    # offer data
    context={
        'dicrect':way_route,
        'map':new_data,
        'lat_s':lat_s,
        'lng_s':lng_s,
        'lat_e':lat_e,
        'lng_e':lng_e,
    }
    return render(request, 'core/success_drawing.html',context)




# globle variable
new_data = []
way_route = []
json_data = ''
class LinkRequest:
    def __init__(self, start_point, end_point):
        Define.__init__(self, start_point, end_point)
        self.start_point = start_point
        self.end_point = end_point

    def get_route(self):
        global new_data
        global json_data
        response = requests.get('https://routing.openstreetmap.de/routed-bike/route/v1/driving/'+self.start_point+';'+self.end_point+'?overview=false&geometries=polyline&steps=true')
        json_data = response.json()
        steps = json_data['routes'][0]['legs'][0]['steps']
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

        way_route = []
        way_loc = json_data['waypoints']

        print(way_route)

        # offer data
        context={
            'dicrect':way_route,
            'map':new_data
        }
        return render(self, 'core/success_drawing.html',context)
    
    def get_direction(self):
        global way_route
        waypoints = json_data['waypoints']
        for waypoint in waypoints:
            routes = waypoint['location']
            for location in routes:
                lat=location
                for location in routes:
                    if location != lat:
                        lng = location
                way_route.append('{lat:'+str(lat)+',lng:'+str(lng)+'}')
        new_way_route = ','.join(way_route) # convert list to string
        way_route = new_way_route
        print(way_route)


class Defines:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

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

    