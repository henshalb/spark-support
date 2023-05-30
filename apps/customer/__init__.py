from flask import Blueprint

from .model.customer import Customer

customer_blueprint = Blueprint('customer', __name__)
