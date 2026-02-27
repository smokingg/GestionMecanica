class Vehiculo:
    def __init__(self, id, cliente_id, patente, marca, modelo, anio, color=""):
        self.id = id
        self.cliente_id = cliente_id  # A qué cliente pertenece
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "patente": self.patente,
            "marca": self.marca,
            "modelo": self.modelo,
            "anio": self.anio,
            "color": self.color
        }

    @staticmethod
    def from_dict(data):
        return Vehiculo(
            id=data["id"],
            cliente_id=data["cliente_id"],
            patente=data["patente"],
            marca=data["marca"],
            modelo=data["modelo"],
            anio=data["anio"],
            color=data.get("color", "")
        )
    