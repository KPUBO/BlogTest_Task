import datetime

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from .base_model import Base


class Post(Base):
    __tablename__ = "Posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    amount_of_likes = Column(Integer, nullable=False, default=0)
