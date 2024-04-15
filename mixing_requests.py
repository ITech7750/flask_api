import requests
import json

# Пример данных для отправки
data = {
    "mixing": [['2022-06-01', '00:00:00', '38.371673583984375', '12.036003112792969', '53.12963104248047'], ['2022-06-01', '00:01:00', '38.345909118652344', '11.206962585449219', '53.11699676513672'], ['2022-06-01', '00:02:00', '38.31132507324219', '11.378925323486328', '53.14986801147461'], ['2022-06-01', '00:03:00', '38.37910461425781', '11.781763076782227', '53.11101150512695']],
    "L" : [1979, 303, 440],
    "d" : [6, 6, 8],
    "D" : [159, 159, 219]
}

try:
    # Отправляем POST-запрос на сервер
    response = requests.post('http://127.0.0.1:5000/api/mixing', json=data)
    
    # Проверяем статус код ответа
    if response.status_code == 200:
        try:
            # Получаем JSON из ответа
            result = response.json()
            print(result)
        except json.decoder.JSONDecodeError:
            print("Response is not in valid JSON format:", response.text)
    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request error:", e)
