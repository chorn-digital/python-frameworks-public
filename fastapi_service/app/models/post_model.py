# fastapi_service/app/models/post_model.py

from sqlalchemy import Column, Integer, String, Text
from fastapi_service.app.config.database import Base


class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)

