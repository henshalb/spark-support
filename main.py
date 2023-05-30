from flask import Flask
from apps.customer import customer_blueprint
from apps.merchant import merchant_blueprint
from apps.user import user_blueprint

from apps import db
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spark.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db = db.init_app(app)
app.register_blueprint(merchant_blueprint)
app.register_blueprint(customer_blueprint)
app.register_blueprint(user_blueprint)


if __name__ == '__main__':
    app.run()
