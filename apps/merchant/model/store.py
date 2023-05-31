from . import db
import os
from werkzeug.utils import secure_filename
from flask import current_app as app


class Store(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)
    store_owner_id = db.Column(
        db.Integer,
        db.ForeignKey('merchants.id'),
        nullable=True
    )
    address = db.Column(db.String(200), nullable=False)