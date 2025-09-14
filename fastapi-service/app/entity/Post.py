from sqlalchemy import Column, Integer, String, Text
from app.config.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, nullable=False)
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)
