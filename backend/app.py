import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.mecanico_routes import mecanico_bp
from routes.cliente_routes import cliente_bp
from routes.vehiculo_routes import vehiculo_bp
from routes.plantilla_routes import plantilla_bp
from routes.orden_routes import orden_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(mecanico_bp, url_prefix="/api/mecanicos")
    app.register_blueprint(cliente_bp, url_prefix="/api/clientes")
    app.register_blueprint(vehiculo_bp, url_prefix="/api/vehiculos")
    app.register_blueprint(plantilla_bp, url_prefix="/api/plantillas")
    app.register_blueprint(orden_bp, url_prefix="/api/ordenes")

    return app