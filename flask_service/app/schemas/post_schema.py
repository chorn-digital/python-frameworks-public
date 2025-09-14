# flask_service/app/schemas/post_schema.py

from marshmallow import Schema, fields


class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    title = fields.Str(required=True, validate=lambda s: len(s) > 0)
    body = fields.Str(required=True)
