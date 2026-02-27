from flask import Blueprint, request, jsonify
from services.vehiculo_service import VehiculoService

vehiculo_bp = Blueprint("vehiculos", __name__)
vehiculo_service = VehiculoService()

@vehiculo_bp.route("/", methods=["GET"])
def obtener_todos():
    vehiculos = vehiculo_service.obtener_todos()
    return jsonify({"ok": True, "vehiculos": vehiculos}), 200

@vehiculo_bp.route("/cliente/<cliente_id>", methods=["GET"])
def obtener_por_cliente(cliente_id):
    vehiculos = vehiculo_service.obtener_por_cliente(cliente_id)
    return jsonify({"ok": True, "vehiculos": vehiculos}), 200

@vehiculo_bp.route("/", methods=["POST"])
def crear():
    datos = request.get_json()

    campos_requeridos = ["cliente_id", "patente", "marca", "modelo", "anio"]
    for campo in campos_requeridos:
        if not datos.get(campo):
            return jsonify({"ok": False, "mensaje": f"El campo {campo} es obligatorio"}), 400

    resultado = vehiculo_service.crear_vehiculo(datos)

    if resultado["ok"]:
        return jsonify(resultado), 201
    else:
        return jsonify(resultado), 400

@vehiculo_bp.route("/<id>", methods=["PUT"])
def editar(id):
    datos = request.get_json()
    resultado = vehiculo_service.editar_vehiculo(id, datos)

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 400