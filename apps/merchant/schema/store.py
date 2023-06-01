from apps import ma
from apps.merchant.model.store import Store


class StoreSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Store
        include_fk = True

    store_name = ma.auto_field()
    store_owner_id = ma.auto_field(required=True)
    address = ma.auto_field()


class StoreListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store
        include_fk = True
        load_instance = True
