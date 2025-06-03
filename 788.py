import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps

API = 'AIzaSyDub0U9BBZPgblPH9oUlkrn69iqpgi8_Bs'

geolocator = GoogleV3(api_key=API)

print(type(geolocator))

name = 'Empire State Building' 
location = geolocator.geocode(name)

print(location.address)
print(location.latitude, location.longitude)

first_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])

print(first_location)

name = 'Marea Restaurant New York' 
location = geolocator.geocode(name)

second_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])

my_locations = pd.concat([first_location, second_location], ignore_index=True)

print(my_locations)
