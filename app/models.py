from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=False)
    priority = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
