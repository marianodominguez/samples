#!/usr/bin/env python

import urllib2
import json
from datetime import datetime

def format_time(time):
	return datetime.fromtimestamp(float(time)/1000)

response = urllib2.urlopen('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson') 
json_data = response.read()

events = json.loads(json_data)

earthquakes = events["features"]

state = "california"

result = filter(lambda e: e["properties"]["type"]=="earthquake" 
	and state.lower() in e["properties"]["place"].lower() , earthquakes)

result = sorted(result, key=lambda e: e["properties"]["mag"], reverse=True)

for e in result:
	print  e["properties"]["title"] , format_time(e["properties"]["time"]), e["properties"]["mag"] 