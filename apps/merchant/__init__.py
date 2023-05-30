from flask import Blueprint

# Models
from .model.store import Store
from .model.merchant import Merchant

merchant_blueprint = Blueprint('merchant', __name__)
