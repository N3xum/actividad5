import pymysql

from app.admin import configuracion_admin
pymysql.install_as_MySQLdb()

from flask import Flask
from config import Config
# CAMBIO: Se agregó "migrate" a las importaciones
from .extensions import db, login_manager, admin, migrate

def create_app():
    app = Flask (__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    admin.init_app(app)
    # CAMBIO: Se inicializó migrate con la app y la db
    migrate.init_app(app, db) 
    
    from .models import User
    from .admin import configuracion_admin
    from .auth import auth_bp
    
    configuracion_admin()
    app.register_blueprint(auth_bp)
    
    return app