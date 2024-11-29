from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from models.base_model import Base

SQLALCHEMY_DATABASE_URL = DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = SessionLocal()

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")

def get_db():
    Base.metadata.create_all(bind=engine)
    try:
        yield Session
    except:
        raise
