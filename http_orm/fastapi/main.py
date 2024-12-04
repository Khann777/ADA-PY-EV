from fastapi import FastAPI

"""
Фреймворк - задает четкую архитектуру, которой вы должны следовать
Библиотека - вы сами решаете, где, как и когда использовать ее инструменты

FastAPI - микро фреймворк, который позволяет писать backend, он не имеет жесткую структуру, и вы сами решаете как организовать папки и приложения
"""

#? app - объект от класса FastAPI, который будет обрабатывать запросы к нашему API (Backend) 
app = FastAPI()

#? uvicorn main:app --reload - команда для запуска локального сервера, main - название файла в котором есть объект от класса FastAPI, :app - название объекта от класса, --reload - флаг, для автоматического обновления

@app.get('/list')
def get_request():
    return {
        'msg': 'get request'
    }

# docs - Документация всего проекта (там хранятся все эндпоинты которые есть в вашем API)

@app.post('/create')
def create_request():
    return {
        'msg': 'created'
    }

@app.delete('/delete')
def delete_request():
    return {
        'msg': 'deleted'
    }
