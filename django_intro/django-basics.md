Django - Фреймворк для разработки веб приложений

DjangoRestFramework (DRF) - надстройка для Django, их отличие заключается в подходах написания приложений 

Django использует подход MVT (Model View Template)
DRF использует MVC (Model View Controller)

**КАК РАЗВЕРНУТЬ ПРИЛОЖЕНИЕ НА DJANGO**
- 
1) Нужно создаю рабочую директорию для проекта
2) Нужно создать файл requirements.txt (в него нужно занести хотя бы базовые библиотеки: psycopg2-binary, djangorestframework, python-decouple)
3) Создание виртуального окружения командой: python3 -m venv venv (и активация)
4) Создаём командой директорию с настройками проекта: (**django-admin startproject config .**) 
                                                         КОМАНДА DJANGO            НАЗВАНИЕ ДИРЕКТОРИИ
В команде django-admin startproject config . - точку нужно обязательно указывать, это делается для того, чтобы убрать вложенность

**КОМАНДЫ DJANGO**
- django-admin startproject config .
- ./manage.py startapp <название приложения> - команда которое создает приложение django
- ./manage.py runserver - запускает локальный сервер на 8000 порту
- 