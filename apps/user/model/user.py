from apps import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    merchants = db.relationship('Merchant', backref='user', lazy=True)
    customers = db.relationship('Customer', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
