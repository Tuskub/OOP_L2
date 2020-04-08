import json
import random

from Observer.interfases.observer import Observer
from Observer.interfases.display import Display


class WeatherStatistics(Observer, Display):
    temp_readings = list()

    def __init__(self):
        self.update()

    def update(self):
        if len(self.temp_readings) > 5:
            del self.temp_readings[0]
        with open('current_weather.json') as f:
            current_state = json.load(f)
        self.temp_readings.append(current_state['fact']['temp'])

    def display(self):
        if len(self.temp_readings) < 5:
            return "Недостаточно данных"
        return f"Максимальная температура: {max(self.temp_readings)}\n" \
               f"Минимальная температура {min(self.temp_readings)}\n" \
               f"Средняя температура: {'%.2f' % (sum(self.temp_readings) / len(self.temp_readings))}"
