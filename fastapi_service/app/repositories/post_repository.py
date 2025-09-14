# fastapi_service/app/repositories/post_repository.py

from sqlalchemy.orm import Session
from fastapi_service.app.models.post_model import PostModel
from fastapi_service.app.schemas.post_schema import PostCreate


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PostModel).offset(skip).limit(limit).all()


def get_post(db: Session, post_id: int):
    return db.query(PostModel).filter(PostModel.id == post_id).first()


def create_post(db: Session, post: PostCreate):
    db_post = PostModel(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, post_id: int, post: PostCreate):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if db_post:
        for key, value in post.dict().items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post
