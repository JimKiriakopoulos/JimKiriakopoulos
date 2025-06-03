x=int(input())
if x<100:
     i=0
     while i < 101:
         x=x+i
         i+=1
print (x)

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyC6rl3bPguYjh7FfEeKGEyqrhFmsapq6g4')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
