import requests


class Bot:

    def __init__(self, token):
        self.token = token
        self.url = 'https://api.telegram.org/bot'
        offset = 0
        self.offset = offset

    def get_message(self):
        data = {'offset': self.offset, 'limit': 0, 'timeout': 0}
        message = requests.post(self.url + self.token + '/getUpdates', data=data)
        return message

    def test_message(self, message):
        if not message.status_code == 200:
            print('false')
            return None
        if not message.json()['ok']:
            print('false')
            return None
        if message.json()['result'] == []:
            return None
        return message

    def confirm_message(self, message):
        for update in message.json()['result']:
            self.offset = update['update_id'] + 1

    def work_with_message(self, message):
        for update in message.json()['result']:
            text = update['message']['text']
            chat_id = update['message']['chat']['id']
            message_id = update['message']['message_id']
        return {'text': text, 'chat_id': chat_id, 'message_id': message_id}

    def post_message_false(self, telegram_message):
        data = {
            'chat_id': telegram_message['chat_id'],
            'text': '<b>' + 'Город не найден!' + '</b>',
            'reply_to_message_id': telegram_message['message_id'],
            'parse_mode': 'HTML'
        }
        requests.post(self.url + self.token + '/sendMessage', data=data)

    def post_massage(self, telegram_message, weather_message):
        data = {
            'chat_id': telegram_message['chat_id'],
            'photo': 'http://openweathermap.org/img/w/' + weather_message['icon'] + '.png',
            'caption': '<b>' + telegram_message["text"] + ':' + '</b>' + weather_message['description'] +
                       '<b>' + 'Температура:' + '</b>' + str(weather_message['temp']) + 'C' +
                       '<b>' + 'Скорость ветра:' + '</b>' + str(weather_message['wind']) + 'м/сек',
            'reply_to_message_id': telegram_message['message_id'],
            'parse_mode': 'HTML'}
        request = requests.post(self.url + self.token + '/sendPhoto', data=data)
        if request == 200:
            return True
        else:
            return False
