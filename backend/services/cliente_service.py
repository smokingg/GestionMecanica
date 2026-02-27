import uuid
from repositories.cliente_repository import ClienteRepository

class ClienteService:
    def __init__(self):
        self.cliente_repo = ClienteRepository()

    def obtener_todos(self):
        return self.cliente_repo.obtener_todos()

    def crear_cliente(self, datos):
        # Verificar que el RUT no exista ya
        existe = self.cliente_repo.buscar_por_rut(datos["rut"])
        if existe:
            return {"ok": False, "mensaje": "Ya existe un cliente con ese RUT"}

        nuevo_cliente = {
            "id": str(uuid.uuid4()),
            "nombre": datos["nombre"],
            "rut": datos["rut"],
            "telefono": datos["telefono"],
            "email": datos.get("email", "")
        }

        self.cliente_repo.guardar(nuevo_cliente)
        return {"ok": True, "mensaje": "Cliente creado exitosamente", "cliente": nuevo_cliente}

    def editar_cliente(self, id, datos):
        cliente = self.cliente_repo.buscar_por_id(id)
        if not cliente:
            return {"ok": False, "mensaje": "Cliente no encontrado"}

        cliente["nombre"] = datos.get("nombre", cliente["nombre"])
        cliente["telefono"] = datos.get("telefono", cliente["telefono"])
        cliente["email"] = datos.get("email", cliente["email"])

        self.cliente_repo.actualizar(cliente)
        return {"ok": True, "mensaje": "Cliente actualizado", "cliente": cliente}