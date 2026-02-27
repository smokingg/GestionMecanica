from flask import Blueprint, request, jsonify
from services.plantilla_service import PlantillaService

plantilla_bp = Blueprint("plantillas", __name__)
plantilla_service = PlantillaService()

@plantilla_bp.route("/", methods=["GET"])
def obtener_todas():
    plantillas = plantilla_service.obtener_todas()
    return jsonify({"ok": True, "plantillas": plantillas}), 200

@plantilla_bp.route("/", methods=["POST"])
def crear():
    datos = request.get_json()

    if not datos.get("nombre"):
        return jsonify({"ok": False, "mensaje": "El nombre es obligatorio"}), 400

    resultado = plantilla_service.crear_plantilla(datos)

    if resultado["ok"]:
        return jsonify(resultado), 201
    else:
        return jsonify(resultado), 400

@plantilla_bp.route("/<id>", methods=["PUT"])
def editar(id):
    datos = request.get_json()
    resultado = plantilla_service.editar_plantilla(id, datos)

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 400

@plantilla_bp.route("/<id>", methods=["DELETE"])
def eliminar(id):
    resultado = plantilla_service.eliminar_plantilla(id)

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 404