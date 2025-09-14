from sqlalchemy.orm import Session
from app.entity import Post
from app.repository import post_repository
from pydantic import BaseModel


class PostController(BaseModel):
    def get_posts(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Post.Post).offset(skip).limit(limit).all()

    def get_post(db: Session, post_id: int):
        return db.query(Post.Post).filter(Post.Post.id == post_id).first()

    def create_post(db: Session, post: post_repository.PostCreate):
        db_post = Post.Post(**post.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    def update_post(db: Session, post_id: int, post: post_repository.PostCreate):
        db_post = db.query(Post.Post).filter(Post.Post.id == post_id).first()
        if db_post:
            db_post.userId = post.userId
            db_post.title = post.title
            db_post.body = post.body
            db.commit()
            db.refresh(db_post)
        return db_post

    def delete_post(db: Session, post_id: int):
        db_post = db.query(Post.Post).filter(Post.Post.id == post_id).first()
        if db_post:
            db.delete(db_post)
            db.commit()
        return db_post
