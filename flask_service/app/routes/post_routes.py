# flask_service/app/routes/post_routes.py

from flask import Blueprint, request, jsonify
from flask_service.app.services import post_service
from flask_service.app.extensions import cache

bp = Blueprint("posts", __name__)


@bp.get("/posts")
@cache.cached(timeout=60, key_prefix="v1_posts_list")
def list_posts():
    posts = post_service.list_posts()
    return jsonify(posts), 200


@bp.get("/posts/<int:post_id>")
def get_post(post_id):
    post = post_service.get_post(post_id)
    return jsonify(post), 200


@bp.post("/posts")
def create_post():
    data = request.get_json() or {}
    post = post_service.create_post(data)
    cache.delete("v1_posts_list")
    return jsonify(post), 201


@bp.put("/posts/<int:post_id>")
@bp.patch("/posts/<int:post_id>")
def update_post(post_id):
    data = request.get_json() or {}
    post = post_service.update_post(post_id, data)
    cache.delete("v1_posts_list")
    return jsonify(post), 200


@bp.delete("/posts/<int:post_id>")
def delete_post(post_id):
    result = post_service.delete_post(post_id)
    cache.delete("v1_posts_list")
    return jsonify(result), 200
