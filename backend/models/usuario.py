# models/usuario.py
# Esto es como una @Entity en Java
# Define cómo se ve un Usuario en nuestro sistema

class Usuario:
    def __init__(self, id, nombre, usuario, password, rol, activo=True):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.password = password
        self.rol = rol          # "admin" o "mecanico"
        self.activo = activo

    def to_dict(self):
        # Convierte el objeto a diccionario para guardarlo en JSON
        return {
            "id": self.id,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password,
            "rol": self.rol,
            "activo": self.activo
        }

    @staticmethod
    def from_dict(data):
        # Convierte un diccionario JSON a objeto Usuario
        return Usuario(
            id=data["id"],
            nombre=data["nombre"],
            usuario=data["usuario"],
            password=data["password"],
            rol=data["rol"],
            activo=data.get("activo", True)
        )