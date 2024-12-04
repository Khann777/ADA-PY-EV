from db_settings import Base, engine

from apps.models import Product

print('СОЗДАЮ МОДЕЛЬ В БД')
Base.metadata.create_all(bind=engine)
print('ТАБЛИЦА УСПЕШНО СОЗДАНА')