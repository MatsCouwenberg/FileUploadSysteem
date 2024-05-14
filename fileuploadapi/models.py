from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base
from pydantic import BaseModel


class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200))
    filename = Column(String(200))
    path = Column(String(900))
    created_at = Column(DateTime, default=func.now())
