
from flask import request
from flask_restful import Resource
from apps.merchant.model.store import Store
from apps import db

from apps.merchant.schema.store import StoreListSchema, StoreSchema


class StoreAPI(Resource):

    def post(self):
        """
        Create store
        """
        try:
            data = request.get_json()
            errors = StoreSchema().validate(data)
            if errors:
                return errors, 400
            store = Store(**data)
            db.session.add(store)
            db.session.commit()
            return StoreSchema().dump(store)
        except Exception:
            # TODO: Specific handlers
            return {"error": "Invalid merchant ID"}, 400

    def get(self):
        """
        Get store by ID or list all
        """
        store_id = request.args.get('id')
        if store_id:
            store = Store.query.get(store_id)
            if store:
                return StoreSchema().dump(store)
            else:
                return {'message': 'Store not found'}, 404
        else:
            stores = Store.query.all()
            return StoreListSchema(many=True).dump(stores)

    def put(self):
        """
        Update store by ID
        """
        store_id = request.args.get('id')
        store = Store.query.get(store_id)
        if store:
            try:
                data = request.get_json()
                errors = StoreSchema().validate(data)
                if errors:
                    return errors, 400

                store.store_name = data.get('store_name', store.store_name)
                store.store_owner_id = data.get(
                    'store_owner_id', store.store_owner_id)
                store.address = data.get('address', store.address)
                store.image = data.get('image', store.image)

                db.session.commit()

                return StoreSchema().dump(store)
            except Exception:
                # TODO: Specific handlers
                return {"error": "Invalid merchant ID"}, 400
        else:
            return {'message': 'Store not found'}, 404

    def delete(self):
        """
        Delete store by ID
        """
        store_id = request.args.get('id')
        store = Store.query.get(store_id)
        if store:
            db.session.delete(store)
            db.session.commit()
            return {'message': 'Store deleted'}
        else:
            return {'message': 'Store not found'}, 404
