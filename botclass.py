import requests


class Bot:

    def __init__(self, token):
        self.token = token
        self.url = 'https://api.telegram.org/bot'

    def get_message(self, offset):
        data = {'offset': offset, 'limit': 0, 'timeout': 0}
        message = requests.post(self.url + self.token + '/getUpdates', data=data)
        return message

    def post_massaage(self, data):
        request = requests.post(self.url + self.token + '/sendMessage', data=data)
        if request == 200:
            return True
        else:
            return False


