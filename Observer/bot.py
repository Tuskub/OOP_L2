import json
import telebot
from telebot import apihelper
from constants.proxyconst import USERNAME, PASSWORD, IP, PORT
from constants.bottoken import TOKEN


bot = telebot.TeleBot(TOKEN)
apihelper.proxy = {'https':f'socks5h://{USERNAME}:{PASSWORD}@{IP}:{PORT}'}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот погоды в Оренбурге!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    with open('response.json') as f:
        templates = json.load(f)
    print(templates)
    if message.text == 'Погода':
        bot.send_message(message.chat.id, f"Погода в Оренбурге: "
                                          f"\nТемпература: {templates['fact']['temp']}\xb0С"
                                          f"\nОщущается как: {templates['fact']['feels_like']}\xb0С"
                                          f"\nСкорость ветра: {templates['fact']['wind_speed']}м/с"
                                          f"\nКртинОчка:  https://yastatic.net/weather/i/icons/blueye/color/svg/{templates['fact']['icon']}.svg")
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()
