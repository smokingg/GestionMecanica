from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

# Blueprint es como un "mini servidor" que agrupa rutas relacionadas
# En vez de tener todas las rutas en un solo archivo gigante
# las separamos por tema (auth, mecanicos, ordenes, etc)
auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()

@auth_bp.route("/login", methods=["POST"])
def login():
    # Recibimos los datos que envía el frontend en formato JSON
    datos = request.get_json()

    # Extraemos usuario y password del diccionario
    nombre_usuario = datos.get("usuario")
    password = datos.get("password")

    # Validamos que vengan los datos
    if not nombre_usuario or not password:
        return jsonify({"ok": False, "mensaje": "Faltan datos"}), 400

    # Le pedimos al Service que procese el login
    resultado = auth_service.login(nombre_usuario, password)

    # Devolvemos el resultado al frontend
    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 401

@auth_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({"ok": True, "mensaje": "Sesión cerrada"}), 200