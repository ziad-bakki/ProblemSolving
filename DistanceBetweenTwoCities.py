import os
import requests
from urllib.parse import quote
from math import radians, sin, cos, asin, sqrt
import json

with open("apikeys.json", "r") as file:
    data = json.load(file)

api = data['geoapify_api_key']


one = input("Input Country 1: ")
two = input("\nInput Country 2: ")

# Encode the inputs
encoded_one = quote(one)
encoded_two = quote(two)

url = f"https://api.geoapify.com/v1/geocode/search?text={encoded_one}&apiKey={api}"
url2 = f"https://api.geoapify.com/v1/geocode/search?text={encoded_two}&apiKey={api}"

headers = {"Accept": "application/json"}

resp = requests.get(url, headers=headers)
resp2 = requests.get(url2, headers=headers)


stats1 = resp.json()
stats2 = resp2.json()

coordinates = stats1['features'][0]['geometry']['coordinates']
coordinates2 = stats2['features'][0]['geometry']['coordinates']



longitude1 = radians(coordinates[0])
latitude1 = radians(coordinates[1])


longitude2 = radians(coordinates2[0])
latitude2 = radians(coordinates2[1])

#radius of earth in kilometers
r = 6371

dlon = longitude2 - longitude1
dlat = latitude2 - latitude1

a = sin(dlat / 2)**2 + cos(latitude1) * cos(latitude2) * sin(dlon / 2)**2

c = 2 * asin(sqrt(a))

distance = (c * r)

print(f"\nThe distance between {one} and {two} is approximately {round(distance, 2)} KM. \n")
