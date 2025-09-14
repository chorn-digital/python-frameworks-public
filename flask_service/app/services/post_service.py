# flask_service/app/services/post_service.py

from flask import abort
from flask_service.app.repositories import post_repository
from flask_service.app.schemas.post_schema import PostSchema

post_schema = PostSchema()
posts_schema = PostSchema(many=True)


def list_posts(skip=0, limit=10):
    posts = post_repository.get_all(skip, limit)
    if not posts:
        abort(404, description="No posts found")
    return posts_schema.dump(posts)


def get_post(post_id: int):
    post = post_repository.get_by_id(post_id)
    if not post:
        abort(404, description="Post not found")
    return post_schema.dump(post)


def create_post(data: dict):
    validated = post_schema.load(data)
    post = post_repository.create(validated)
    return post_schema.dump(post)


def update_post(post_id: int, data: dict):
    post = post_repository.get_by_id(post_id)
    if not post:
        abort(404, description="Post not found")
    validated = post_schema.load(data, partial=True)
    updated = post_repository.update(post, validated)
    return post_schema.dump(updated)


def delete_post(post_id: int):
    post = post_repository.get_by_id(post_id)
    if not post:
        abort(404, description="Post not found")
    post_repository.delete(post)
    return {"deleted": post_id}
