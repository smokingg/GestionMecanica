class Cliente:
    def __init__(self, id, nombre, rut, telefono, email=""):
        self.id = id
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "rut": self.rut,
            "telefono": self.telefono,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        return Cliente(
            id=data["id"],
            nombre=data["nombre"],
            rut=data["rut"],
            telefono=data["telefono"],
            email=data.get("email", "")
        )