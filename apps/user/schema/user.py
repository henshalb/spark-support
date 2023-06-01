from apps import ma
from apps.user.model.user import User


class UserInSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class UserOutSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    role = ma.String()


class UserLoginSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    email = ma.auto_field()
    password = ma.auto_field()


class UserUpdateSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = ma.auto_field(required=False)
    first_name = ma.auto_field(required=False)
    last_name = ma.auto_field(required=False)
    email = ma.auto_field(required=False)
    phone = ma.auto_field(required=False)
    role = ma.String(required=False)

