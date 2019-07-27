from django.shortcuts import render
import requests,json

# globle variable
new_data = []
way_route = []
json_data = ''
class LinkRequest:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
    def get_way_point(self,request):
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
        # offer data
        context={
            'map':new_data
        }
        return render(request, 'core/success_drawing.html',context)


class WayRoute(LinkRequest):
    def __init__(self, start_point, end_point, urls):
        LinkRequest.__init__(self, start_point, end_point)
        self.url = urls

    def get_direction(self,request):
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
