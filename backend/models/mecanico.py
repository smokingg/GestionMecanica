class Mecanico:
    def __init__(self, id, nombre, usuario, password, especialidad, activo=True):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.password = password
        # La especialidad es lo que sabe hacer
        # Ejemplo: "Frenos", "Motor", "Electricidad"
        self.especialidad = especialidad
        self.activo = activo

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password,
            "especialidad": self.especialidad,
            "activo": self.activo
        }

    @staticmethod
    def from_dict(data):
        return Mecanico(
            id=data["id"],
            nombre=data["nombre"],
            usuario=data["usuario"],
            password=data["password"],
            especialidad=data.get("especialidad", ""),
            activo=data.get("activo", True)
        )