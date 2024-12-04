from db_settings import Base, engine

from app.models import Product

print("СОЗДАЮ МОДЕЛЬ В ДБ")
Base.metadata.create_all(engine)
print("ТАБЛИЦА УСПЕШНО СОЗДАНА")