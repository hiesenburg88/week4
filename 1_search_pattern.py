# Divvy Bikes

import json
from urllib.request import urlopen
import math

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']

young_latitude = 41.793414
young_longitude = -87.600915

winning_distance = 10000000


for station in stations:
  station_latitude = float(station['latitude'])
  station_longitude = float(station['longitude'])

  latitude_delta = math.fabs(station_latitude - young_latitude)
  longitude_delta = math.fabs(station_longitude - young_longitude)
  distance_to_this_station = math.hypot(latitude_delta, longitude_delta)


  if distance_to_this_station < winning_distance:
    winning_distance = distance_to_this_station
    winning_station = station
    print("The distance from Young to", station['stationName'], ": ", distance_to_this_station)



print()
print("The nearest station is:", winning_station["stationName"])
print("There are", winning_station["availableBikes"], "bikes there right now!")
