from dataclasses import dataclass
from pyowm import OWM
from skills import factory
from datetime import datetime
from utils import wav_name

from ai import AI


class Weather():
    # Ubicación de la que queremos sacar la informacion
    __location = "Arrecife, ES"
    # API KEY
    api_key = "69fb7f1f7d1bcddca9763495a9baeb02"

    def __init__(self):
        self.ow = OWM(api_key=self.api_key)
        self.mgr = self.ow.weather_manager()

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
            print("Detailed Status:", detail_status)
            print("Pressure:", pressure)
            print("Humidity:", humidity)
            print("Temperature:", temperature)
            print("UVI:", uvi)
            forecast_text = f"Today's forecast includes {detail_status} conditions, with an average pressure of {pressure} and a humidity index of {humidity}%. As for the temperature, it's maintaining a cool demeanor at around {temperature} degrees Celsius."
            print(forecast_text)
            return forecast_text
        except Exception as e:
            print(e)

@dataclass
class WeatherSkill:
    name = 'weather_skill'

    def commands(self, _):
        return ['tiempo', 'reporte del tiempo', 'como esta el dia', 'dame el reporte del tiempo']

    def handle_command(self, _, ai: AI):
        myweather = Weather()

        hoy = datetime.now()
        dia_hoy = hoy.strftime("%d-%m-%Y")

        ai.say(myweather.forecast(), wav_name(self,index=dia_hoy))


def initialize():
    factory.register(WeatherSkill.name, WeatherSkill)
