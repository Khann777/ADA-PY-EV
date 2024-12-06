from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from decouple import config

db_url = f'postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_NAME')}'

engine = create_engine(db_url)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)