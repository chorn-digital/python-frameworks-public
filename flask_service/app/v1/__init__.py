from flask import Blueprint

bp = Blueprint("v1", __name__)
from . import post_route_v1  # noqa
