from . import db


class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # address = db.Column(db.String(200), nullable=False)

    # One-to-many relationship with Merchant
    merchants = db.relationship('Merchant', backref='store', lazy=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address
