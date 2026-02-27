from flask import Blueprint, request, jsonify
from services.mecanico_service import MecanicoService

mecanico_bp = Blueprint("mecanicos", __name__)
mecanico_service = MecanicoService()

# Obtener todos los mecánicos
@mecanico_bp.route("/", methods=["GET"])
def obtener_todos():
    mecanicos = mecanico_service.obtener_todos()
    return jsonify({"ok": True, "mecanicos": mecanicos}), 200

# Obtener solo mecánicos activos
@mecanico_bp.route("/activos", methods=["GET"])
def obtener_activos():
    mecanicos = mecanico_service.obtener_activos()
    return jsonify({"ok": True, "mecanicos": mecanicos}), 200

# Crear mecánico
@mecanico_bp.route("/", methods=["POST"])
def crear():
    datos = request.get_json()

    # Validamos que vengan los campos obligatorios
    campos_requeridos = ["nombre", "usuario", "password"]
    for campo in campos_requeridos:
        if not datos.get(campo):
            return jsonify({"ok": False, "mensaje": f"El campo {campo} es obligatorio"}), 400

    resultado = mecanico_service.crear_mecanico(datos)

    if resultado["ok"]:
        return jsonify(resultado), 201
    else:
        return jsonify(resultado), 400

# Editar mecánico
@mecanico_bp.route("/<id>", methods=["PUT"])
def editar(id):
    datos = request.get_json()
    resultado = mecanico_service.editar_mecanico(id, datos)

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 400

# Desactivar mecánico
@mecanico_bp.route("/<id>/desactivar", methods=["PUT"])
def desactivar(id):
    resultado = mecanico_service.desactivar_mecanico(id)

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 404
