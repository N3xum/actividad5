from flask_login import UserMixin
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True ,nullable = False)
    # password = db.Column(db.String(100), nullable = False)
    # Se aumentó la longitud a 255 porque el hash utiliza 160 caracteres como minimo y para que asi el hash de la contraseña entre completo
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(100), default="user")
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

#Se agregó nueva tabla Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)