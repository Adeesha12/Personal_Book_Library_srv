from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError
from typing import Annotated

DB_NAME = 'fastapi_db'
DB_USERNAME = 'postgres'
DB_PASSWORD = 'mysecretpassword'
DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/{DB_NAME}'
engine = create_engine(DATABASE_URI)
try:
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"Database '{DB_NAME}' created successfully!")
    engine = create_engine(DATABASE_URI)

except OperationalError as e:
    print("An error occurred:", e)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
