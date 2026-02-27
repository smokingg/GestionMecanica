from datetime import datetime

class Orden:
    def __init__(self, id, mecanico_id, cliente_id, vehiculo_id,
                 fecha_ingreso, hora_llegada, descripcion, tareas,
                 estado="pendiente", colacion=None, fecha_creacion=None):
        self.id = id
        self.mecanico_id = mecanico_id
        self.cliente_id = cliente_id
        self.vehiculo_id = vehiculo_id
        self.fecha_ingreso = fecha_ingreso
        self.hora_llegada = hora_llegada
        self.descripcion = descripcion
        # tareas es una lista de dicts con nombre y completada
        self.tareas = tareas
        # estado puede ser: pendiente, en_proceso, terminado
        self.estado = estado
        # colacion guarda inicio, fin y duración
        self.colacion = colacion or {
            "inicio": None,
            "fin": None,
            "duracion_minutos": None
        }
        # Si no viene fecha_creacion usamos la fecha actual
        self.fecha_creacion = fecha_creacion or datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "mecanico_id": self.mecanico_id,
            "cliente_id": self.cliente_id,
            "vehiculo_id": self.vehiculo_id,
            "fecha_ingreso": self.fecha_ingreso,
            "hora_llegada": self.hora_llegada,
            "descripcion": self.descripcion,
            "tareas": self.tareas,
            "estado": self.estado,
            "colacion": self.colacion,
            "fecha_creacion": self.fecha_creacion
        }

    @staticmethod
    def from_dict(data):
        return Orden(
            id=data["id"],
            mecanico_id=data["mecanico_id"],
            cliente_id=data["cliente_id"],
            vehiculo_id=data["vehiculo_id"],
            fecha_ingreso=data["fecha_ingreso"],
            hora_llegada=data["hora_llegada"],
            descripcion=data.get("descripcion", ""),
            tareas=data.get("tareas", []),
            estado=data.get("estado", "pendiente"),
            colacion=data.get("colacion"),
            fecha_creacion=data.get("fecha_creacion")
        )
