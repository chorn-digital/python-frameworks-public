# fastapi_service/app/services/post_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi_service.app.repositories import post_repository
from fastapi_service.app.schemas.post_schema import PostCreate


def list_posts(db: Session, skip: int = 0, limit: int = 10):
    return post_repository.get_posts(db, skip, limit)


def get_post_by_id(db: Session, post_id: int):
    post = post_repository.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PostModel not found")
    return post


def create_post(db: Session, post: PostCreate):
    return post_repository.create_post(db, post)


def update_post(db: Session, post_id: int, post: PostCreate):
    db_post = post_repository.update_post(db, post_id, post)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PostModel not found")
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = post_repository.delete_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PostModel not found")
    return db_post
