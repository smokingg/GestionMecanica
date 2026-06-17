import uuid
from repositories.usuario_repository import UsuarioRepository
from repositories.mecanico_repository import MecanicoRepository

class AuthService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()
        self.mecanico_repo = MecanicoRepository()

    def login(self, nombre_usuario, password):
        # Paso 1: Buscar en usuarios (admin)
        usuario = self.usuario_repo.buscar_por_usuario(nombre_usuario)

        if usuario:
            if not usuario["activo"]:
                return {"ok": False, "mensaje": "Usuario desactivado"}
            if usuario["password"] != password:
                return {"ok": False, "mensaje": "Contraseña incorrecta"}
            return {
                "ok": True,
                "mensaje": "Login exitoso",
                "usuario": {
                    "id": usuario["id"],
                    "nombre": usuario["nombre"],
                    "rol": usuario["rol"]
                }
            }

        # Paso 2: Buscar en mecánicos
        mecanico = self.mecanico_repo.buscar_por_usuario(nombre_usuario)

        if mecanico:
            if not mecanico["activo"]:
                return {"ok": False, "mensaje": "Usuario desactivado"}
            if mecanico["password"] != password:
                return {"ok": False, "mensaje": "Contraseña incorrecta"}
            return {
                "ok": True,
                "mensaje": "Login exitoso",
                "usuario": {
                    "id": mecanico["id"],
                    "nombre": mecanico["nombre"],
                    "rol": "mecanico"
                }
            }

        return {"ok": False, "mensaje": "Usuario no encontrado"}