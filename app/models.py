from sqlalchemy import Column, Integer, String
from .database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), nullable=False)
    event_type = Column(String(100), nullable=False)