from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.hotel import Hotel
from models.room import Room
from models.guest import Guest

DATABASE_URL = 'sqlite:///hotel_management.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()
