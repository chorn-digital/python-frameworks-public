# flask_service/app/repositories/post_repository.py

from flask_service.app.extensions import db
from flask_service.app.models.post_model import PostModel


def get_all(skip=0, limit=10):
    return db.session.query(PostModel).offset(skip).limit(limit).all()


def get_by_id(post_id: int):
    return db.session.get(PostModel, post_id)


def create(data: dict):
    post = PostModel(**data)
    db.session.add(post)
    db.session.commit()
    return post


def update(post: PostModel, data: dict):
    for key, value in data.items():
        setattr(post, key, value)
    db.session.commit()
    return post


def delete(post: PostModel):
    db.session.delete(post)
    db.session.commit()
    return post
