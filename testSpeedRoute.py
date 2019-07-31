from time import strftime,gmtime
import json,requests,datetime
# response = requests.get('http://localhost/datas_json/data_car.json')
response = requests.get('https://routing.openstreetmap.de/routed-car/route/v1/driving/104.822,11.5237;104.8893,11.5558?overview=false&geometries=polyline&steps=true&annotations=true')
store = response.json()

data = [
	'steps',
	'annotation']
steps = store['routes'][0]['legs'][0][data[0]]
annotation = store['routes'][0]['legs'][0][data[1]]

speeds = annotation['speed']
durations = annotation['duration']
distances = annotation['distance']

# print(store)
# print(steps)
# print(annotation)
# print(distance)
# print(distance)

time = 0
print(len(durations))
for times in durations:
	time = time+times
print('duration :',time*4.07,strftime("%Hh:%Mm:%Ss", gmtime(time*4.07)))
length = 0
for distance in distances:
	length = length+distance
print('distance :',length)

avg_speed = 0
for speed in speeds:
	avg_speed = avg_speed+speed
print('avg_speed :',avg_speed/len(speeds))

print('time :',length/653.9)