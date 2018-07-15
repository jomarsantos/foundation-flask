from app.main import ma
from app.user import User
from marshmallow import Schema, fields

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
    email = fields.Email(required=True)

user_schema = UserSchema(exclude=[
    'password',
    'date_created',
    'birthday',
])

class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

user_login_schema = UserLoginSchema()
