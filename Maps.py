# This code is developed by Mister Rohan Kumar Bhoi
# Instagram ID : i_am_the_rohan
# facebook : facebook.com/rohan.bhoi.07
# Mail ID : rohanbhoi1546@gmail.com
# My Blog : www.technicalrohan07.blogspot.com
# Linkdi : rohan-kumar-bhoi
# Twitter : Rohan_KumarBhoi

import pandas as pd
import numpy as np
import folium
#import os
import webbrowser
from pynput.keyboard import *
import keyboard
#from click import command
from time import sleep

import pyttsx3
#import wikipedia
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)
#engine.say("Hello ! Good Morning Sir..!")
#engine.say("I am jarvis, Your personal assistent !")
#engine.say("I like to inform that, it is a simulation of real maps !")
#engine.say("Which is designed and developed by, Master Rohan Kumar Bhoi !")
#engine.say("Please select an location, which you want to search !")
#engine.say("Sir do you like to open yesterdays, workmodel to continue ?")
#engine.say("If you want to continue, please press enter button two times..!")
#engine.runAndWait()

while keyboard.read_key() == 'shift':
    data = {'city':[input("Enetr an city name : ").capitalize()]}
    df = pd.DataFrame(data)
    df
    print(df)

    from geopy.exc import GeocoderTimedOut 
    from geopy.geocoders import Nominatim 

    longitude = [] 
    latitude = []

    def findGeoCode(city):
        try:
            geolocator = Nominatim(user_agent="Rohan's_Maps_Project")
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
        map = folium.Map(location=[x, y],zoom_start=550)
        map.add_child(folium.Marker(location=[x, y]))
        for h in (df["city"]):
            name = i
        place = name+'.html'
        site = map.save(place)
        print(place)


        webbrowser.open_new_tab(place)

        sleep(5) 
        print("Press the 'Shift' key if you want to continue sir ! ")
        #engine.say("Press the 'Shift' key if you want to continue sir ! ")
        #engine.runAndWait()

    except:
        print("")
        engine.say("Some thing went wrong  !")
        print("")
        engine.say("Hope this location is Right !")
        print("")
        sleep(5) 
        engine.say("Press the 'Shift' key if you want to continue sir ! ")
        engine.runAndWait()

engine.say("Thanks for using ")
