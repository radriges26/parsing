import requests
from pprint import pprint

# Имя пользователя github
username = "radriges26"

# url для запроса
url = f"https://api.github.com/users/{username}/repos"

# делаем запрос и возвращаем json
user_data = requests.get(url).json()

# довольно распечатать данные JSON
for i in user_data:
    print(i['name'])