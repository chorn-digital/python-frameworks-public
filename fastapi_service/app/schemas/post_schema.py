# fastapi_service/app/schemas/post_schema.py

from pydantic import BaseModel


class PostBase(BaseModel):
    user_id: int
    title: str
    body: str


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int

    class Config:
        orm_mode = True

