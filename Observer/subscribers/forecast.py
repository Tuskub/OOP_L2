import json
import random

from Observer.interfases.observer import Observer
from Observer.interfases.display import Display


class Forecast(Observer, Display):
    pressure_readings = list()

    def __init__(self):
        self.update()

    def update(self):
        if len(self.pressure_readings) > 5:
            del self.pressure_readings[0]
        with open('current_weather.json') as f:
            current_state = json.load(f)
        self.pressure_readings.append(current_state['fact']['pressure_mm'])

    def __forecast_weather(self):
        avr_pressure = sum(self.pressure_readings[:-1]) / (len(self.pressure_readings) - 1)
        if self.pressure_readings[-1] < avr_pressure:
            return 'Погода ухудшается'
        else:
            return 'Погода улучшается'

    def display(self):
        if len(self.pressure_readings) < 5:
            return "Недостаточно данных"
        return self.__forecast_weather()
