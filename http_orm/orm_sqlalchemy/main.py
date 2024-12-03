from decouple import config

from sqlalchemy import create_engine, Integer, Column, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

"""
ORM (Object-Relational Mapping) - Способ взаимодействия с БД при помощи python(Объектно-Ориентированных моделей)
Вместо написания сырых SQL запросов, мы можем использовать объекты, которые связаны с таблицами в БД.
ORM позволяет:
1. Работать с данными используя аттрибуты и методы
2. Не писать сырые SQL запросы
3. Избежать SQL инъекций


SQLALCHEMY - ORM 
SQLAMCHEMY делится на 2 части
1. Core - низкоуровневая работу с SQL, написание запросов вручную
2. ORM - высокоуровневый компонент, который позволяет работать с БД используя python-классы
"""

#* db_url отвечает за связь с базой данных
#* db_url = f'driver://user:password@db_host/db_name'
db_url = f'postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_NAME')}'

#* engine отвечает за подключение к БД, и работу с ней
engine = create_engine(db_url)

#* Base является базовым классом для моделей
#* Модель - классовое представление того, как выглядит таблица в БД
Base = declarative_base()

#* Sessionlocal - фабрика для создания сессий для работы с БД, эти сессии нужны для выполнения транакций
Sessionlocal = sessionmaker(bind=engine)

session = Sessionlocal()

#* Создание модели Product, эта модель будет являться представлением таблицы "products" в БД
class Product(Base):
    __tablename__ = 'products' #? __tablename__ - передается название таблицы для БД
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)

    def __str__(self):
        return f'title={self.title}, price={self.price}, quantity={self.quantity}'
    
#* Создаем все таблицы, если они еще не были созданы
Base.metadata.create_all(bind=engine)

#! CRUD

#? 1 -  C (Create)
product1 = Product(title='iphone', price=1200.50, quantity=3) #* Создаем объект
session.add(product1) #* Добавляем объект в сессию
session.commit() #* Фиксируем изменения в таблице в БД
print(f'В таблицу добавлен новый товар: {product1}')

#? 2 -  R (Read)
products = session.query(Product).all() #* SELECT * FROM products;
# for product in products:
#     print(product)

#? 3 -  U (Update)
product = session.query(Product).filter(Product.title == 'iphone').first()
if product:
    product.price = 2000
    product.quantity = 10
    product.title = 'samsung'
    session.commit() #* Фиксируем изменения товара в таблице
    print(f"Успешно измениои товар: {product}")

#? 4 -  D (Delete)
session.delete(product)
session.commit()
print(f'Удалили запись: {product}')
