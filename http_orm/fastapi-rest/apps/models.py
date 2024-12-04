from sqlalchemy import Column, Integer, String, Float, Text
from db_settings import Base

class Product(Base):
    __tablename__: str = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
    description = Column(Text)