from time import strftime,gmtime
import json,requests,datetime
response = requests.get('http://localhost/datas_json/data_car.json')
# response = requests.get('https://routing.openstreetmap.de/routed-car/route/v1/driving/104.822,11.5237;104.8893,11.5558?overview=false&geometries=polyline&steps=true&annotations=true')
store = response.json()

data = [
	'steps',
	'annotation'
]
steps = store['routes'][0]['legs'][0][data[0]]
annotation = store['routes'][0]['legs'][0][data[1]]

speeds = annotation['speed']
durations = annotation['duration']
distances = annotation['distance']

time = 0
# print(len(durations))
for times in durations:
	time = time+times
print('duration :',time*4.07,strftime("%Hh:%Mm:%Ss", gmtime(time*4.07)))

length = 0
for distance in distances:
	length = length+distance
# print('distance :',length)

avg_speed = 0
for speed in speeds:
	avg_speed = avg_speed+speed
# print('avg_speed :',avg_speed/len(speeds))

# print('time :',length/avg_speed)

insert_count = 0
intersection_count = 0
insert_start = [
	[104.866659, 11.56289],
	[104.869783, 11.562741],
	[104.870274, 11.562725],
	[104.870819, 11.562708],
	[104.870749, 11.561871],
	[104.870677, 11.56103],
	[104.870637, 11.560516],
	[104.870596, 11.560034],
	[104.870573, 11.55974],
]
num_s=len(insert_start)-1
index_e = insert_start[num_s][0]
count_location = 0

final_data = []
# print(steps[2]['intersections'][0]['location'])
for step in steps:
	intersections = step['intersections']
	for intersection in intersections:
		locations = intersection['location']
		if locations[0]<insert_start[0][0]<insert_start[num_s][0]:
			final_data.append(locations)
			count_location = count_location+1
			# insert start
		elif insert_start[0][0]<locations[0]<insert_start[num_s][0]:
			final_data.append(insert_start)
			insert_count=insert_count+num_s
			#insert end
		elif locations[0]>insert_start[num_s][0]:
			final_data.append(locations)
			count_location = count_location+1
# print(insert_start[insert_count])
print(final_data)
		# print(locations)
intersection_count = intersection_count+1








print('Items :',len(durations),'[***] length intersections :',intersection_count,'[***] Location :',count_location)
