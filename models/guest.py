from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Guest(Base):
    __tablename__ = 'guests'
    
    id = Column(Integer, primary_key=True)
    nationality = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    room = relationship('Room', back_populates='guests')
