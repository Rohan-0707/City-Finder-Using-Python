import pandas as pd
import numpy as np
import folium
import os
import webbrowser

data = {'city':[input("Enetr an city name : ")]}
df = pd.DataFrame(data)
df
print(df)

from geopy.exc import GeocoderTimedOut 
from geopy.geocoders import Nominatim 

longitude = [] 
latitude = []

def findGeoCode(city):
    try:
        geolocator = Nominatim(user_agent="your_app_name")
        return geolocator.geocode(city)
    except GeocoderTimedOut:
        return findGeoCode(city)

try:
    for i in (df["city"]):
        if findGeoCode(i) != None:
            loc = findGeoCode(i)
            latitude.append(loc.latitude) 
            longitude.append(loc.longitude)
        else:
            latitude.append(np.nan) 
            longitude.append(np.nan)

    df["Longitude"] = longitude 
    df["Latitude"] = latitude

    print(df)

    x = float(latitude[0])
    y = float(longitude[0])
    print(x)
    print(y)
    map = folium.Map(location=[x, y],zoom_start=350)
    map.add_child(folium.Marker(location=[x, y]))
    for h in (df["city"]):
        name = i
    place = name+'.html'
    site = map.save(place)
    print(place)


    webbrowser.open_new_tab(place)

finally:
    print("")
    print("Some thing went wrong  !")
    print("")
    print("Hope this location is Right !")
    print("")