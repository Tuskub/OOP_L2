import json
import requests
from constants.apikey import YA_WEATHER_KEY


res = requests.get('https://api.weather.yandex.ru/v1/informers?lat=51.7682&lon=55.097',
                   headers={'X-Yandex-API-Key': YA_WEATHER_KEY})
res.raise_for_status()
res.raw.decode_content = True
data = res.json()
with open('response.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
