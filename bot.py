from botclass import Bot
from weather import Weather
import time
from settings import APPID, TOKEN, WEATHER_SERVER

bot = Bot(TOKEN)
weather = Weather(APPID=APPID, WEATHER_SERVER=WEATHER_SERVER)

while True:
    time.sleep(3)
    message = bot.get_message()
    message = bot.test_message(message)

    if message == None:
        continue

    bot.confirm_message(message)
    print(message.json())
    message = bot.work_with_message(message)
    print(message['text'])
    print(message)
    answer = weather.get_weather(location=message['text'])
    if answer == None:
        bot.post_message_false(telegram_message=message)
        continue
    print(answer)

    bot.post_massage(telegram_message=message, weather_message=answer)
