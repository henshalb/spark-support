from apps import db
from apps.customer.model.customer import Customer
from apps.merchant.model.merchant import Merchant
from apps.user.model.user import RoleEnum, User


def create_user(**kwargs):
    password = kwargs.pop("password")
    new_user = User(**kwargs)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    if kwargs.get("role") == RoleEnum.MERCHANT:
        record = Merchant(
            name=f"Merchant <{kwargs.get('name')}>",
            user_id=new_user.id
        )
    else:
        record = Customer(
            name=f"Customer <{kwargs.get('name')}>",
            user_id=new_user.id
        )

    db.session.add(record)
    db.session.commit()

    return new_user


def get_user(email):
    return User.query.filter_by(email=email).first()
