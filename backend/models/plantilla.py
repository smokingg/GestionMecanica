class Plantilla:
    def __init__(self, id, nombre, tareas):
        self.id = id
        self.nombre = nombre
        # tareas es una lista de strings
        # Ejemplo: ["Cambio de aceite", "Cambio de filtro", "Revisión de frenos"]
        self.tareas = tareas

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tareas": self.tareas
        }

    @staticmethod
    def from_dict(data):
        return Plantilla(
            id=data["id"],
            nombre=data["nombre"],
            tareas=data.get("tareas", [])
        )