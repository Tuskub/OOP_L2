import json
import requests
from typing import List
from Observer.constants.apikey import YA_WEATHER_KEY, LAT, LON
from Observer.interfases.subject import Subject
from Observer.interfases.observer import Observer


class WeatherData(Subject):
    __current_state = None
    __subscribers: List[Observer] = []

    def __init__(self):
        # self.__update_current_state()
        return

    def register_observer(self, subscriber):
        self.__subscribers.append(subscriber)
        return

    def remove_observer(self, subscriber):
        self.__subscribers.remove(subscriber)
        return

    def notify_observer(self):
        for s in self.__subscribers:
            s.update()
        return

    @staticmethod
    def __update_current_state():
        res = requests.get(f'https://api.weather.yandex.ru/v1/informers?lat={LAT}&lon={LON}',
                           headers={'X-Yandex-API-Key': YA_WEATHER_KEY})
        res.raise_for_status()
        res.raw.decode_content = True
        data = res.json()
        with open('current_weather.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return

    def measurements_update(self):
        self.__update_current_state()
        self.notify_observer()
        return
