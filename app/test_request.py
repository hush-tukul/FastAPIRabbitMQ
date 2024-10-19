import requests

# URL вашего FastAPI приложения
url = "http://localhost:8000/register"

# Данные для отправки (здесь вы можете указать нужный email)
data = {
    "email": "user@example.com"
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Проверка статуса ответа
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
