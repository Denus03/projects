import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('5802252395:AAFYOizfgr0kB-quV5TOjErnpeldIshchn4')


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,f'Привіт, я бот, а ти я так розумію {message.from_user.first_name}\n/start - запуск бота\n/help - команди бота\n/credits - автор бота\nщоб дізнатись погоду напишіть назву міста')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/start - запуск бота\n/help - команди бота\n/credits - автор бота\nщоб дізнатись погоду напишіть назву міста')


@bot.message_handler(func=lambda message: True)
def test(message):
    try:
        place = message.text.split("/text")[-1]

        config_dict = get_default_config()
        config_dict['language'] = 'ua'

        owm = OWM('c21634f76b5a9a6f1618d84281e65f38')
        #place = input("Введіть назву міста")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather

        temp = w.temperature("celsius")
        temp1 = temp['temp']
        temp2 = temp['feels_like']
        temp3 = temp['temp_max']
        temp4 = temp['temp_min']

        wi = w.wind()['speed']
        humi = w.humidity
        st = w.status
        dt = w.detalied_status
        ti = w.reference_time('iso')
        pr = w.pressure['press']
        vd = w.visibility_distance

        bot.send_message(message.chat.id,f"""В місті {place} температура str(temp1)C°\n +"
                         максимальна температура(temp3)C° \n
                         мінімальна температур(temp4)C° \n
                         відчувається як(temp2)C° \n
                         швидкість вітру(wi)м/с \n
                         тиск(pr)мм.рт \n
                         вологість(humi)% \n
                         видимість(vd)метрів
                         "статус(st) \n\n (dt)""")
    except:
        bot.send_message(message.chat.id, "Такого міста не знайдено")
        print(str(message.text), "- не знайдено")


bot.polling(none_stop=True, interval=1)
