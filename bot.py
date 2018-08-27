import requests
from botclass import Bot
import time
from settings import APPID, TOKEN, WEATHER_SERVER

offset = 0


def get_weather(location):
    res = requests.get(WEATHER_SERVER + location,
                       params={'units': 'metric', 'lang': 'ru', 'APPID': APPID})
    return res


bot = Bot(TOKEN)

while True:
    time.sleep(3)
    message = bot.get_message(offset=offset)

    if not message.status_code == 200:
        print('false')
        continue
    if not message.json()['ok']:
        print('false')
        continue
    if message.json()['result'] == []:
        continue

    for update in message.json()['result']:
        offset = update['update_id'] + 1

    for update in message.json()['result']:
        text = update['message']['text']
    print(message.json())
    location = 'Bishkek,KG'
    result = get_weather(location)
    print(result.json())
    if not result.status_code == 200:
        data = {
            'chat_id': update['message']['chat']['id'],
            'text': 'ошибка',
            'reply_to_message_id': update['message']['message_id'],
            'parse_mode': 'HTML'
        }
    for weathers in result.json()['list']:
        temp = weathers['main']['temp']
        wind = weathers['wind']['speed']
        descr = weathers['weather'][0]['description']
    print(descr)
    thend = "температура - " + str(temp) +"! " + "скорость ветра - " + str(wind) + "!! " + "описание - " + descr + "!!!"
    data = {
        'chat_id': update['message']['chat']['id'],
        'text': thend,
        'reply_to_message_id': update['message']['message_id'],
        'parse_mode': 'HTML'
    }
    bot.post_massaage(data=data)
