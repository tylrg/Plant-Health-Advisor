#!/usr/bin/env python
import sys
from twython import Twython
import random
import pyowm
import time

owm= pyowm.OWM(API_key='08ecab7ec3081e73f292598b28b53b62')
apiKey = "K6Hso0OsudmpCRpYoHpPUdhKt"
apiSecret = "oALIksO0R7P9maX0G4KIo1ICv4eC0ODZvBRhoKeav9iWUzyLo5"
accessToken = "832293691888918533-xPRRik0FVZhASooHK6VH0e8Q2BQ47a6"
accessTokenSecret = "MnYkHzZedctJ7QH0oz3Tryh9pfIU2fNqpuR4ht67AHFXr"

cv=0
wv= 0
tv= 0
tempHi=0
tempLow=0
moistHi=0
moistLow=0


handle=raw_input('Please enter your twitter handle(w/o the @): ')


place= raw_input('Please enter your city name: ')
print('Selcted City: '+place+'\n')

print('Plant List:\naloe,basil,cactus,catnip,parsely,rose,tomato,tulip\n')
plant=raw_input('Please enter your plant name from the list above: ')
print('Selcted Plant: '+plant+'\n')


if plant == 'aloe':
    tempHi=100
    tempLow=35
    moistLow=20
elif plant == 'basil':
    tempHi=100
    tempLow=45
    moistLow=30
elif plant == 'cactus':
    tempHi85
    tempLow=45
    moistLow=10
elif plant =='catnip':
    tempHi=100
    tempLow=40
    moistLow=30
elif plant == 'parsely':
    tempHi=100
    tempLow=28
    moistLow=30
elif plant == 'rose':
    tempHi=100
    tempLow=10
    moistLow=30
elif plant == 'tomato':
    tempHi=95
    tempLow=65
    moistLow=30
elif plant == 'tulip':
    tempHi=100
    tempLow=60
    moistLow=30



while True:

    observation = owm.weather_at_place(place+'us')
    w= observation.get_weather()



    wv=w.get_humidity()
    tv=w.get_temperature('fahrenheit')['temp']
    cv=w.get_clouds()
    print('Current Weather Status: ')
    print(tv)
    print(wv)
    print(cv)


    if (cv>50):
        print'______________________________________________'
        tweetStr = '@'+handle+' It is cloudy out; make sure the plant gets enough sunlight!'
        api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
        api.update_status(status=tweetStr)
        print ('Tweeted' + tweetStr)
        print'______________________________________________'

    if (tv>tempHi):
        print'______________________________________________'
        tweetStr = '@'+handle+' It is hot out; make sure the plant gets enough water!'
        api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
        api.update_status(status=tweetStr)
        print ('Tweeted' + tweetStr)
        print'______________________________________________'


    if (tv<tempLow):
        print'______________________________________________'
        tweetStr = '@'+handle+' It is cold out; make sure the plant is warm enough!'
        api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
        api.update_status(status=tweetStr)
        print ('Tweeted' + tweetStr)
        print'______________________________________________'


    if (wv<moistLow):
        print'______________________________________________'
        tweetStr = '@'+handle+' It is dry out; make sure the plant is gets enough water!'
        api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
        api.update_status(status=tweetStr)
        print ('Tweeted: ' + tweetStr)
        print'______________________________________________'

    time.sleep(86400)



