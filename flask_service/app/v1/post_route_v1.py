# flask_service/app/v1/post_route_v1.py

from flask import request, jsonify
from flask_service.app.v1 import bp
from flask_service.app.extensions import db, cache
from flask_service.app.models import PostModel


@bp.get("/posts")
@cache.cached(timeout=60, key_prefix="v1_posts_list")
def list_posts():
    posts = db.session.execute(db.select(PostModel)).scalars().all()
    if not posts:
        abort(404, description="PostModel not found")

    return jsonify([p.to_dict() for p in posts]), 200


@bp.get("/posts/<int:post_id>")
def get_post(post_id):
    post = db.session.get(PostModel, post_id)
    if not post:
        abort(404, description="PostModel not found")
    return jsonify(post.to_dict()), 200


@bp.post("/posts")
def create_post():
    data = request.get_json() or {}
    post = PostModel(userId=data.get("userId"), title=data.get("title"), body=data.get("body"))
    db.session.add(post)
    db.session.commit()
    cache.delete("v1_posts_list")
    return jsonify(post.to_dict()), 201


@bp.put("/posts/<int:post_id>")
@bp.patch("/posts/<int:post_id>")
def update_post(post_id):
    post = db.session.get(PostModel, post_id)
    if not post:
        abort(404, description="PostModel not found")
    data = request.get_json() or {}
    for k in ("userId", "title", "body"):
        if k in data:
            setattr(post, k, data[k])
    db.session.commit()
    cache.delete("v1_posts_list")
    return jsonify(post.to_dict()), 200


@bp.delete("/posts/<int:post_id>")
def delete_post(post_id):
    post = db.session.get(PostModel, post_id)
    if not post:
        abort(404, description="PostModel not found")
    db.session.delete(post)
    db.session.commit()
    cache.delete("v1_posts_list")
    return jsonify({"deleted": post_id}), 200
