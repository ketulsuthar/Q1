from flask import Flask

from flask_login import LoginManager

from db import db
from models import User
from resources.user import auth as auth_blueprint
from resources.main import main as main_blueprint
from data import USERS

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # Suppresses warning while tracking modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        return USERS.get('admin')

        # return User.query.get(int(user_id))

    with app.app_context():
        import models

        db.create_all()

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app


app = create_app()


if __name__ == "__main__":
  #    app = create_app()
  print(" Starting app...")
  app.run(host="0.0.0.0", port=5004)