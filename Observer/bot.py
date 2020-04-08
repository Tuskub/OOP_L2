# Стандартные библиотеки
import time
from threading import Thread
# Библиотека для выполнения команд в определенное время
import schedule
# Библиотеки для работы с Telegram API
import telebot
from telebot import apihelper, types
# Константы
from constants.proxyconst import USERNAME, PASSWORD, IP, PORT
from constants.bottoken import TOKEN
# Классы из реализации наблюдателя
from Observer.weather import WeatherData
from Observer.subscribers.current_conditions import CurrentConditions
from Observer.subscribers.statistic import WeatherStatistics
from Observer.subscribers.forecast import Forecast


bot = telebot.TeleBot(TOKEN)
apihelper.proxy = {'https':f'socks5h://{USERNAME}:{PASSWORD}@{IP}:{PORT}'}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот погоды в Оренбурге!')


@bot.message_handler(commands=['help'])
def help_message(message):
    help_info = 'Данный бот предназначен для вывода информации о погоде в Оренбурге!\n' \
                'Список команд:\n' \
                '\'Погода\' - для вывода информации актуальной информации о погоде\n' \
                '\'Статистика\' - для вывода статистической информации о температуре\n' \
                '\'Прогноз\' - для получения прогноза погоды на ближайшие полчаса\n'
    bot.send_message(message.chat.id, help_info)


@bot.message_handler(content_types=['text'])
def send_text(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='По данным Яндекс.Погоды', url='https://yandex.ru/pogoda/orenburg')
    markup.add(btn_my_site)
    if message.text == 'Погода':
        bot.send_message(message.chat.id, cs.display(), reply_markup=markup)
    elif message.text == 'Статистика':
        bot.send_message(message.chat.id, stat.display(), reply_markup=markup)
    elif message.text == 'Прогноз':
        bot.send_message(message.chat.id, forecast.display(), reply_markup=markup)


def start_bot():
    bot.polling(none_stop=True)


def update_weather():
    # wd.measurements_update()
    bot.send_message(394068509, 'Саня')
    # bot.send_message(430265734, 'Женя')


def update_data():
    schedule.every().hour.at(":00").do(update_weather)
    schedule.every().hour.at(":30").do(update_weather)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    wd = WeatherData()
    cs = CurrentConditions()
    stat = WeatherStatistics()
    forecast = Forecast()

    wd.register_observer(cs)
    wd.register_observer(stat)
    wd.register_observer(forecast)

    t1 = Thread(target=start_bot)
    t2 = Thread(target=update_data)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

