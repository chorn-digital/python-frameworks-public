# flask_service/app/factory.py

from flask import Flask
from flask_service.app.config import config_by_name
from flask_service.app.extensions import db, migrate, jwt, cache
from flask_service.app.routes import post_routes


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cache.init_app(app)

    # Register blueprints
    app.register_blueprint(post_routes.bp, url_prefix="/api/v1")

    # Error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    from flask import jsonify

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found", "message": error.description}), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request", "message": error.description}), 400
