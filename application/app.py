from flask import Flask
from .db import db
from .fights_bp import fights_bp
from .fighters_bp import fighters_bp
from .bet_bp import bet_bp
from .weight_class_bp import weight_class_bp
from database_script.populate_database import populate_database


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/UFC"

    db.init_app(app)

    with app.app_context():

        db.create_all()

        populate_database()

    app.register_blueprint(fights_bp)
    app.register_blueprint(fighters_bp)
    app.register_blueprint(bet_bp)
    app.register_blueprint(weight_class_bp)

    return app


