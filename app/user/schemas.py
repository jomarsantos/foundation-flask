from app.main import ma
from app.user import User
from marshmallow import post_load, fields

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
    email = fields.Email()

user_schema = UserSchema()
users_schema = UserSchema(many=True)
