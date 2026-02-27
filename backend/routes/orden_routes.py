from flask import Blueprint, request, jsonify
from services.orden_service import OrdenService

orden_bp = Blueprint("ordenes", __name__)
orden_service = OrdenService()

# Obtener todas las órdenes
@orden_bp.route("/", methods=["GET"])
def obtener_todas():
    ordenes = orden_service.obtener_todas()
    return jsonify({"ok": True, "ordenes": ordenes}), 200

# Obtener órdenes por fecha
@orden_bp.route("/fecha/<fecha>", methods=["GET"])
def obtener_por_fecha(fecha):
    ordenes = orden_service.obtener_por_fecha(fecha)
    return jsonify({"ok": True, "ordenes": ordenes}), 200

# Obtener órdenes de un mecánico en una fecha
@orden_bp.route("/mecanico/<mecanico_id>/fecha/<fecha>", methods=["GET"])
def obtener_por_mecanico_y_fecha(mecanico_id, fecha):
    ordenes = orden_service.obtener_por_mecanico_y_fecha(mecanico_id, fecha)
    return jsonify({"ok": True, "ordenes": ordenes}), 200

# Crear orden
@orden_bp.route("/", methods=["POST"])
def crear():
    datos = request.get_json()

    campos_requeridos = ["mecanico_id", "cliente_id", "vehiculo_id", "fecha_ingreso", "hora_llegada"]
    for campo in campos_requeridos:
        if not datos.get(campo):
            return jsonify({"ok": False, "mensaje": f"El campo {campo} es obligatorio"}), 400

    resultado = orden_service.crear_orden(datos)

    if resultado["ok"]:
        return jsonify(resultado), 201
    else:
        return jsonify(resultado), 400

# Cambiar estado de la orden
@orden_bp.route("/<id>/estado", methods=["PUT"])
def cambiar_estado(id):
    datos = request.get_json()

    if not datos.get("estado"):
        return jsonify({"ok": False, "mensaje": "El campo estado es obligatorio"}), 400

    resultado = orden_service.cambiar_estado(id, datos["estado"])

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 400

# Completar una tarea
@orden_bp.route("/<id>/tarea", methods=["PUT"])
def completar_tarea(id):
    datos = request.get_json()

    if not datos.get("nombre_tarea"):
        return jsonify({"ok": False, "mensaje": "El campo nombre_tarea es obligatorio"}), 400

    resultado = orden_service.completar_tarea(id, datos["nombre_tarea"])

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 400

# Iniciar colación
@orden_bp.route("/<id>/colacion/iniciar", methods=["PUT"])
def iniciar_colacion(id):
    resultado = orden_service.iniciar_colacion(id)

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 400

# Terminar colación
@orden_bp.route("/<id>/colacion/terminar", methods=["PUT"])
def terminar_colacion(id):
    resultado = orden_service.terminar_colacion(id)

    if resultado["ok"]:
        return jsonify(resultado), 200
    else:
        return jsonify(resultado), 400