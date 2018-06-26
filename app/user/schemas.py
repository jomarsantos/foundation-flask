from app.main import ma
from app.user import User
from marshmallow import post_load

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    @post_load
    def make_instance(self, data):
        try:
            return User(**data)
        except Exception as e:
            print('Bad data for User: {}'.format(data))
            raise e

user_schema = UserSchema()
users_schema = UserSchema(many=True)
