from flask import Blueprint, request, jsonify
from services.cliente_service import ClienteService

cliente_bp = Blueprint("clientes", __name__)
cliente_service = ClienteService()

@cliente_bp.route("/", methods=["GET"])
def obtener_todos():
    clientes = cliente_service.obtener_todos()
    return jsonify({"ok": True, "clientes": clientes}), 200

@cliente_bp.route("/", methods=["POST"])
def crear():
    datos = request.get_json()

    campos_requeridos = ["nombre", "rut", "telefono"]
    for campo in campos_requeridos:
        if not datos.get(campo):
            return jsonify({"ok": False, "mensaje": f"El campo {campo} es obligatorio"}), 400

    resultado = cliente_service.crear_cliente(datos)

    if resultado["ok"]:
        return jsonify(resultado), 201
    else:
        return jsonify(resultado), 400

@cliente_bp.route("/<id>", methods=["PUT"])
def editar(id):
    datos = request.get_json()
    resultado = cliente_service.editar_cliente(id, datos)

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 400