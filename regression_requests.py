import requests
import json

# Пример данных для отправки
data = {
    "regression_kip": [['01.01.2021', '0:00', '334.6292725'], ['01.01.2021', '0:01', '334.6299133'], ['01.01.2021', '0:02', '334.6305542'], ['01.01.2021', '0:03', '334.6311951']],
    "regression_la": [['03.01.2021', '2:00', '2.1'], ['07.01.2021', '2:00', '1.9'], ['10.01.2021', '2:00', '2.3'], ['12.01.2021', '2:00', '2.5']]
}

try:
    # Отправляем POST-запрос на сервер
    response = requests.post('http://127.0.0.1:5000/api/regression', json=data)
    
    # Проверяем статус код ответа
    if response.status_code == 200:
        try:
            # Пытаемся получить JSON из ответа
            result = response.json()
            print(result)
        except json.decoder.JSONDecodeError:
            print("Response is not in valid JSON format:", response.text)
    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request error:", e)
