import requests


class Weather:

    def __init__(self, APPID, WEATHER_SERVER):
        self.appid = APPID
        self.weather_server = WEATHER_SERVER

    def get_weather(self, location):
        result = requests.get(self.weather_server + location,
                              params={'units': 'metric', 'lang': 'ru', 'APPID': self.appid})
        if not result.status_code == 200:
            return None
        result = result.json()
        if result['list'] == []:
            return None
        else:

            for weathers in result['list']:
                temp = weathers['main']['temp']
                wind = weathers['wind']['speed']
                description = weathers['weather'][0]['description']
                icon = weathers['weather'][0]['icon']
            res = {'temp': temp, 'wind': wind, 'description': description, 'icon': icon}
            return res
