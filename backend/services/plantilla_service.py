import uuid
from repositories.plantilla_repository import PlantillaRepository

class PlantillaService:
    def __init__(self):
        self.plantilla_repo = PlantillaRepository()

    def obtener_todas(self):
        return self.plantilla_repo.obtener_todas()

    def crear_plantilla(self, datos):
        # tareas debe ser una lista de strings
        # Ejemplo: ["Cambio de aceite", "Cambio de filtro"]
        if not datos.get("tareas") or len(datos["tareas"]) == 0:
            return {"ok": False, "mensaje": "La plantilla debe tener al menos una tarea"}

        nueva_plantilla = {
            "id": str(uuid.uuid4()),
            "nombre": datos["nombre"],
            "tareas": datos["tareas"]
        }

        self.plantilla_repo.guardar(nueva_plantilla)
        return {"ok": True, "mensaje": "Plantilla creada", "plantilla": nueva_plantilla}

    def editar_plantilla(self, id, datos):
        plantilla = self.plantilla_repo.buscar_por_id(id)
        if not plantilla:
            return {"ok": False, "mensaje": "Plantilla no encontrada"}

        plantilla["nombre"] = datos.get("nombre", plantilla["nombre"])
        plantilla["tareas"] = datos.get("tareas", plantilla["tareas"])

        self.plantilla_repo.actualizar(plantilla)
        return {"ok": True, "mensaje": "Plantilla actualizada", "plantilla": plantilla}

    def eliminar_plantilla(self, id):
        plantilla = self.plantilla_repo.buscar_por_id(id)
        if not plantilla:
            return {"ok": False, "mensaje": "Plantilla no encontrada"}

        self.plantilla_repo.eliminar(id)
        return {"ok": True, "mensaje": "Plantilla eliminada"}