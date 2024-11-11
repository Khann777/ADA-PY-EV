from decouple import config

# Токен для бота
TELEGRAM_API_TOKEN = config('TELEGRAM_API_TOKEN')

# Параметры подключения к базе данных
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
