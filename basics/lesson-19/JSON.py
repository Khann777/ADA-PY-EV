'=============================================JSON======================================'
# Javascript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных почти для всех языков программирования

"""
Сериализация - Перевод с python объектов в JSON строку

Десериализация - перевод из JSON строки в python объекты
"""

import json

"""
.dumps() - Метод для сериализации в json строку

.dump() - метод для сериализации в json файл
"""

user_data = {
    'email': 'nikita@gmail.com',
    'password': '123321',
    'is_active': False,
    'access': None
}

with open('user_data.json', 'w') as file:
    json.dump(user_data, file)
 

json_string = json.dumps(user_data)
print('JSON строка:', json_string)

"""
loads() - метод для десериализации с json строки

load() - метод для десериализации с json файла
"""

with open('user_data.json', 'r') as file:
    python_data = json.load(file)
    print(python_data, 'Десериализация')

python_dict = json.loads(json_string)
print(python_dict, 'С JSON строки')