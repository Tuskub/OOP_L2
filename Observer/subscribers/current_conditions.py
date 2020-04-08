import datetime
import json

from Observer.interfases.observer import Observer
from Observer.interfases.display import Display


class CurrentConditions(Observer, Display):
    temp = None
    feels_like = None
    wind_speed = None
    obs_time = None

    def __init__(self):
        self.update()

    def update(self):
        with open('current_weather.json') as f:
            current_state = json.load(f)
        self.temp = current_state['fact']['temp']
        self.feels_like = current_state['fact']['feels_like']
        self.wind_speed = current_state['fact']['wind_speed']
        self.obs_time = current_state['fact']['obs_time']
        return

    def display(self):
        return f"Погода в Оренбурге({datetime.datetime.fromtimestamp(self.obs_time)}):" \
               f"\nТемпература: {self.temp}\xb0С" \
               f"\nОщущается как: {self.feels_like}\xb0С" \
               f"\nСкорость ветра: {self.wind_speed}м/с"
