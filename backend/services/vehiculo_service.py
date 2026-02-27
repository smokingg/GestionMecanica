import uuid
from repositories.vehiculo_repository import VehiculoRepository
from repositories.cliente_repository import ClienteRepository

class VehiculoService:
    def __init__(self):
        self.vehiculo_repo = VehiculoRepository()
        self.cliente_repo = ClienteRepository()

    def obtener_todos(self):
        return self.vehiculo_repo.obtener_todos()

    def obtener_por_cliente(self, cliente_id):
        return self.vehiculo_repo.obtener_por_cliente(cliente_id)

    def crear_vehiculo(self, datos):
        # Verificar que el cliente existe
        cliente = self.cliente_repo.buscar_por_id(datos["cliente_id"])
        if not cliente:
            return {"ok": False, "mensaje": "Cliente no encontrado"}

        # Verificar que la patente no exista ya
        existe = self.vehiculo_repo.buscar_por_patente(datos["patente"])
        if existe:
            return {"ok": False, "mensaje": "Ya existe un vehículo con esa patente"}

        nuevo_vehiculo = {
            "id": str(uuid.uuid4()),
            "cliente_id": datos["cliente_id"],
            "patente": datos["patente"].upper(),
            "marca": datos["marca"],
            "modelo": datos["modelo"],
            "anio": datos["anio"],
            "color": datos.get("color", "")
        }

        self.vehiculo_repo.guardar(nuevo_vehiculo)
        return {"ok": True, "mensaje": "Vehículo creado exitosamente", "vehiculo": nuevo_vehiculo}

    def editar_vehiculo(self, id, datos):
        vehiculo = self.vehiculo_repo.buscar_por_id(id)
        if not vehiculo:
            return {"ok": False, "mensaje": "Vehículo no encontrado"}

        vehiculo["marca"] = datos.get("marca", vehiculo["marca"])
        vehiculo["modelo"] = datos.get("modelo", vehiculo["modelo"])
        vehiculo["anio"] = datos.get("anio", vehiculo["anio"])
        vehiculo["color"] = datos.get("color", vehiculo["color"])

        self.vehiculo_repo.actualizar(vehiculo)
        return {"ok": True, "mensaje": "Vehículo actualizado", "vehiculo": vehiculo}