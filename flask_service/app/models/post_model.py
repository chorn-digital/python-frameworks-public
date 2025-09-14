# flask_service/app/models/post_model.py

from flask_service.app.extensions import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Post {self.id} - {self.title}>"
