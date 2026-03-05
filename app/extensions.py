from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
# CAMBIO: Se importó Migrate
from flask_migrate import Migrate 

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name="Panel Administrador")
# CAMBIO: Se inicializó Migrate
migrate = Migrate() 

# COMENTADO: login_manager.login_view = "login"
# CAMBIO: Se corrigió la ruta indicando que viene del blueprint "auth"
login_manager.login_view = "auth.login"