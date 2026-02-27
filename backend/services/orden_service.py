import uuid
from datetime import datetime
from repositories.orden_repository import OrdenRepository
from repositories.mecanico_repository import MecanicoRepository
from repositories.cliente_repository import ClienteRepository
from repositories.vehiculo_repository import VehiculoRepository

class OrdenService:
    def __init__(self):
        self.orden_repo = OrdenRepository()
        self.mecanico_repo = MecanicoRepository()
        self.cliente_repo = ClienteRepository()
        self.vehiculo_repo = VehiculoRepository()

    def obtener_todas(self):
        return self.orden_repo.obtener_todas()

    def obtener_por_mecanico_y_fecha(self, mecanico_id, fecha):
        return self.orden_repo.obtener_por_mecanico_y_fecha(mecanico_id, fecha)

    def obtener_por_fecha(self, fecha):
        return self.orden_repo.obtener_por_fecha(fecha)

    def crear_orden(self, datos):
        # Verificar que el mecánico existe
        mecanico = self.mecanico_repo.buscar_por_id(datos["mecanico_id"])
        if not mecanico:
            return {"ok": False, "mensaje": "Mecánico no encontrado"}

        # Verificar que el cliente existe
        cliente = self.cliente_repo.buscar_por_id(datos["cliente_id"])
        if not cliente:
            return {"ok": False, "mensaje": "Cliente no encontrado"}

        # Verificar que el vehículo existe
        vehiculo = self.vehiculo_repo.buscar_por_id(datos["vehiculo_id"])
        if not vehiculo:
            return {"ok": False, "mensaje": "Vehículo no encontrado"}

        # Convertimos las tareas de la plantilla al formato de la orden
        # Cada tarea empieza con completada = False
        tareas = []
        for tarea in datos.get("tareas", []):
            tareas.append({
                "nombre": tarea,
                "completada": False
            })

        nueva_orden = {
            "id": str(uuid.uuid4()),
            "mecanico_id": datos["mecanico_id"],
            "cliente_id": datos["cliente_id"],
            "vehiculo_id": datos["vehiculo_id"],
            "fecha_ingreso": datos["fecha_ingreso"],
            "hora_llegada": datos["hora_llegada"],
            "descripcion": datos.get("descripcion", ""),
            "tareas": tareas,
            "estado": "pendiente",
            "colacion": {
                "inicio": None,
                "fin": None,
                "duracion_minutos": None
            },
            "fecha_creacion": datetime.now().isoformat()
        }

        self.orden_repo.guardar(nueva_orden)
        return {"ok": True, "mensaje": "Orden creada exitosamente", "orden": nueva_orden}

    def cambiar_estado(self, id, nuevo_estado):
        # Verificar que el estado sea válido
        estados_validos = ["pendiente", "en_proceso", "terminado"]
        if nuevo_estado not in estados_validos:
            return {"ok": False, "mensaje": f"Estado inválido. Debe ser: {estados_validos}"}

        orden = self.orden_repo.buscar_por_id(id)
        if not orden:
            return {"ok": False, "mensaje": "Orden no encontrada"}

        orden["estado"] = nuevo_estado
        self.orden_repo.actualizar(orden)
        return {"ok": True, "mensaje": f"Estado actualizado a {nuevo_estado}", "orden": orden}

    def completar_tarea(self, orden_id, nombre_tarea):
        orden = self.orden_repo.buscar_por_id(orden_id)
        if not orden:
            return {"ok": False, "mensaje": "Orden no encontrada"}

        # Buscamos la tarea por nombre y la marcamos como completada
        tarea_encontrada = False
        for tarea in orden["tareas"]:
            if tarea["nombre"] == nombre_tarea:
                tarea["completada"] = True
                tarea_encontrada = True
                break

        if not tarea_encontrada:
            return {"ok": False, "mensaje": "Tarea no encontrada"}

        self.orden_repo.actualizar(orden)
        return {"ok": True, "mensaje": "Tarea completada", "orden": orden}

    def iniciar_colacion(self, orden_id):
        orden = self.orden_repo.buscar_por_id(orden_id)
        if not orden:
            return {"ok": False, "mensaje": "Orden no encontrada"}

        # No puede iniciar colación si ya hay una activa
        if orden["colacion"]["inicio"] and not orden["colacion"]["fin"]:
            return {"ok": False, "mensaje": "Ya hay una colación activa"}

        orden["colacion"]["inicio"] = datetime.now().isoformat()
        orden["colacion"]["fin"] = None
        orden["colacion"]["duracion_minutos"] = None

        self.orden_repo.actualizar(orden)
        return {"ok": True, "mensaje": "Colación iniciada", "orden": orden}

    def terminar_colacion(self, orden_id):
        orden = self.orden_repo.buscar_por_id(orden_id)
        if not orden:
            return {"ok": False, "mensaje": "Orden no encontrada"}

        # Verificar que haya una colación activa
        if not orden["colacion"]["inicio"]:
            return {"ok": False, "mensaje": "No hay colación activa"}

        # Calculamos cuántos minutos duró la colación
        inicio = datetime.fromisoformat(orden["colacion"]["inicio"])
        fin = datetime.now()
        duracion = round((fin - inicio).total_seconds() / 60, 1)

        orden["colacion"]["fin"] = fin.isoformat()
        orden["colacion"]["duracion_minutos"] = duracion

        self.orden_repo.actualizar(orden)
        return {"ok": True, "mensaje": f"Colación terminada. Duración: {duracion} minutos", "orden": orden}