import uuid
from repositories.usuario_repository import UsuarioRepository

class AuthService:
    def __init__(self):
        # El Service crea su propio Repository para usarlo
        self.usuario_repo = UsuarioRepository()

    def login(self, nombre_usuario, password):
        # Paso 1: Buscar el usuario en el JSON
        usuario = self.usuario_repo.buscar_por_usuario(nombre_usuario)

        # Paso 2: Si no existe devolvemos error
        if usuario is None:
            return {"ok": False, "mensaje": "Usuario no encontrado"}

        # Paso 3: Si está desactivado devolvemos error
        if not usuario["activo"]:
            return {"ok": False, "mensaje": "Usuario desactivado"}

        # Paso 4: Verificar la contraseña
        if usuario["password"] != password:
            return {"ok": False, "mensaje": "Contraseña incorrecta"}

        # Paso 5: Todo correcto, devolvemos los datos del usuario
        return {
            "ok": True,
            "mensaje": "Login exitoso",
            "usuario": {
                "id": usuario["id"],
                "nombre": usuario["nombre"],
                "rol": usuario["rol"]
            }
        }