from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Import and register blueprints
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.industry_routes import industry_bp
    app.register_blueprint(industry_bp)

    from app.routes.storage_routes import storage_bp
    app.register_blueprint(storage_bp)

    from app.routes.item_routes import item_bp
    app.register_blueprint(item_bp)

    from app.routes.expense_routes import expense_bp
    app.register_blueprint(expense_bp)

    from app.routes.trade_routes import trade_bp
    app.register_blueprint(trade_bp)

    from app.routes.transact_routes import transact_bp
    app.register_blueprint(transact_bp)

    from app.routes.inventory_routes import inventory_bp
    app.register_blueprint(inventory_bp)

    return app
