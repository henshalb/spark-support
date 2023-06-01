from flask import Blueprint
from flask_restful import Api

# Models
from .model.store import Store
from .model.merchant import Merchant

merchant_blueprint = Blueprint('merchant', __name__)
merchant_api = Api(merchant_blueprint)

from .api.store import StoreAPI
from .api.merchant import MerchantStoreAPI
merchant_api.add_resource(StoreAPI, '/store')
merchant_api.add_resource(MerchantStoreAPI, '/merchantStore')
