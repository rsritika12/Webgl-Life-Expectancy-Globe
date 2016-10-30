from geopy import geocoders
from geopy.geocoders import GoogleV3
import time
g = geocoders.GoogleV3()
f = open('countries2005.txt','r')
fParse = f.readlines()
countries = []
for i in range(len(fParse)):
    countries.append(fParse[i].strip('\n'))
for country in countries:  #gets lat and long for each country
    placemark = g.geocode(country)
    print (country,placemark.latitude,placemark.longitude)
    time.sleep(.5)   
for i in range(len(fParse)):
    countries.append(fParse[i].strip('\n'))
