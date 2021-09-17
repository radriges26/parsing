import requests
import json

appid = '9c64bdaa5c48353f38dc024280efdac7' # апи ключ для авторизации

service = 'https://api.openweathermap.org/data/2.5/weather' # ссылка сервиса
req = requests.get(f'{service}?q=Ufa&appid={appid}&units=metric') # передаём параметры
data = json.loads(req.text)

print(f"В городе {data['name']} {data['main']['temp']} градусов по Цельсию, скорость ветра: {data['wind']['speed']}")

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)