#!/usr/bin/env python
from pyowm import OWM
import os
import sys
owm = OWM(os.environ['OPENWEATHER_API_KEY'])
obs = owm.weather_at_place(os.environ['CITY_NAME'])
weather = obs.get_weather()
status = weather.get_detailed_status()
temperature = weather.get_temperature('celsius')['temp']
humidity = weather.get_humidity()
print "Source=openweathermap, city=",os.environ['CITY_NAME'],",description=",status,",temp=",temperature,",humidity=",humidity
f = open("/var/log/syslog", "a")
f.writelines(["Source=openweathermap, city="])
f.writelines(os.environ['CITY_NAME'])
f.writelines([",description="])
f.writelines(status)
f.writelines([",temp="])
f.write(str(temperature))
f.writelines([",humidity="])
f.write(str(humidity))
f.writelines(["\n"])

