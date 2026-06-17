import os

from flask import Flask
from flask_login import LoginManager

from config import Config
from extensions import db
from models import User


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from routes.admin import admin_bp
    from routes.auth import auth_bp
    from routes.cart import cart_bp
    from routes.orders import orders_bp
    from routes.shop import shop_bp

    app.register_blueprint(shop_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(admin_bp)

    @app.context_processor
    def inject_cart_count():
        from flask_login import current_user

        count = 0
        if current_user.is_authenticated:
            from models import CartItem

            count = CartItem.query.filter_by(user_id=current_user.id).count()
        return dict(cart_count=count)

   return app
app = create_app()
