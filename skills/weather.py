from dataclasses import dataclass
from pyowm import OWM
from geopy import Nominatim, location
from datetime import datetime
from skills import factory

from ai import AI

class Weather():
    # Ubicación de la que queremos sacar la informacion
    __location = "Valencia, ES"
    # API KEY
    api_key = "69fb7f1f7d1bcddca9763495a9baeb02"
    
    def __init__(self):
        self.ow = OWM(api_key=self.api_key)
        self.mgr = self.ow.weather_manager()

        city = "Valencia"
        country = "ES"
        self.__location = city + ", " + country

        
    @property
    def weather(self):
        forecast = self.mgr.weather_at_place(self.__location)
        return forecast
    
    def forecast(self):
        try:
            forecast = self.mgr.weather_at_place(self.__location)
            detail_status = forecast.weather.detailed_status
            pressure = forecast.weather.pressure['press']
            humidity = forecast.weather.humidity
            temperature = forecast.weather.temperature("celsius")['temp']
            uvi = forecast.weather.uvi
            print("Detailed Status:",detail_status)
            print("Pressure:",pressure)
            print("Humidity:",humidity)
            print("Temperature:",temperature)
            print("UVI:",uvi)
        except Exception as e:
            print(e)
            
@dataclass
class Weather_skill:
    name = 'weather_skill'

    def commands(self, command:str):
        return ['weather', 'forecast', 'what is the weather like', 'give me the forecast',"what's the weather","what's the weather like"]

    def handle_command(self, command:str, ai:AI):
        myweather = Weather()
        forecast = myweather.forecast
        ai.say(forecast)
        return forecast

def initialize():
    factory.register(Weather_skill.name, Weather_skill)