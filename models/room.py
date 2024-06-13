from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Room(Base):
    __tablename__ = 'rooms'
    
    id = Column(Integer, primary_key=True)
    room_number = Column(Integer, nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    hotel = relationship('Hotel', back_populates='rooms')
    guests = relationship('Guest', back_populates='room')
