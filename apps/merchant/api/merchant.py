
from flask_restful import Resource
from apps.merchant.model.store import Store
from flask import request

from apps.merchant.schema.store import StoreListSchema


class MerchantStoreAPI(Resource):

    """
    Stores of a merchant
    """

    def get(self):
        merchant_id = request.args.get('id')
        if not merchant_id:
            return {"status": "Merchant identifier is required"}, 400
        stores = Store.query.filter_by(store_owner_id=merchant_id).all()
        return StoreListSchema(many=True).dump(stores)
