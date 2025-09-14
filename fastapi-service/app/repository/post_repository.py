from pydantic import BaseModel


class PostBase(BaseModel):
    userId: int
    title: str
    body: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True
