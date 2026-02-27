import uuid
from repositories.mecanico_repository import MecanicoRepository
from repositories.usuario_repository import UsuarioRepository

class MecanicoService:
    def __init__(self):
        self.mecanico_repo = MecanicoRepository()
        self.usuario_repo = UsuarioRepository()

    def obtener_todos(self):
        return self.mecanico_repo.obtener_todos()

    def obtener_activos(self):
        return self.mecanico_repo.obtener_activos()

    def crear_mecanico(self, datos):
        # Verificar que el usuario no exista ya en mecanicos
        existe_mecanico = self.mecanico_repo.buscar_por_usuario(datos["usuario"])
        if existe_mecanico:
            return {"ok": False, "mensaje": "El usuario ya existe"}

        # Verificar que el usuario no exista en usuarios (admin)
        existe_usuario = self.usuario_repo.buscar_por_usuario(datos["usuario"])
        if existe_usuario:
            return {"ok": False, "mensaje": "El usuario ya existe"}

        # Creamos el nuevo mecánico
        # uuid4() genera un ID único aleatorio
        # str() lo convierte a texto
        nuevo_mecanico = {
            "id": str(uuid.uuid4()),
            "nombre": datos["nombre"],
            "usuario": datos["usuario"],
            "password": datos["password"],
            "especialidad": datos.get("especialidad", ""),
            "activo": True
        }

        self.mecanico_repo.guardar(nuevo_mecanico)
        return {"ok": True, "mensaje": "Mecánico creado exitosamente", "mecanico": nuevo_mecanico}

    def editar_mecanico(self, id, datos):
        # Verificar que el mecánico existe
        mecanico = self.mecanico_repo.buscar_por_id(id)
        if not mecanico:
            return {"ok": False, "mensaje": "Mecánico no encontrado"}

        # Actualizamos solo los campos que llegaron
        # El .get(campo, valor_actual) significa:
        # "si el campo viene en datos úsalo, sino deja el que ya tenía"
        mecanico["nombre"] = datos.get("nombre", mecanico["nombre"])
        mecanico["especialidad"] = datos.get("especialidad", mecanico["especialidad"])
        mecanico["activo"] = datos.get("activo", mecanico["activo"])

        # Solo actualizamos password si vino en los datos
        if datos.get("password"):
            mecanico["password"] = datos["password"]

        self.mecanico_repo.actualizar(mecanico)
        return {"ok": True, "mensaje": "Mecánico actualizado", "mecanico": mecanico}

    def desactivar_mecanico(self, id):
        mecanico = self.mecanico_repo.buscar_por_id(id)
        if not mecanico:
            return {"ok": False, "mensaje": "Mecánico no encontrado"}

        mecanico["activo"] = False
        self.mecanico_repo.actualizar(mecanico)
        return {"ok": True, "mensaje": "Mecánico desactivado"}

