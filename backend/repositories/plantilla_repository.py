import json
import os

class PlantillaRepository:
    def __init__(self):
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.ruta_json = os.path.join(raiz, "data", "plantillas.json")

    def _leer_plantillas(self):
        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar_plantillas(self, plantillas):
        with open(self.ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(plantillas, archivo, indent=4, ensure_ascii=False)

    def obtener_todas(self):
        return self._leer_plantillas()

    def buscar_por_id(self, id):
        plantillas = self._leer_plantillas()
        for plantilla in plantillas:
            if plantilla["id"] == id:
                return plantilla
        return None

    def guardar(self, plantilla_dict):
        plantillas = self._leer_plantillas()
        plantillas.append(plantilla_dict)
        self._guardar_plantillas(plantillas)

    def actualizar(self, plantilla_actualizada):
        plantillas = self._leer_plantillas()
        for i, plantilla in enumerate(plantillas):
            if plantilla["id"] == plantilla_actualizada["id"]:
                plantillas[i] = plantilla_actualizada
                break
        self._guardar_plantillas(plantillas)

    def eliminar(self, id):
        plantillas = self._leer_plantillas()
        # Guardamos todas MENOS la que tiene ese id
        plantillas = [p for p in plantillas if p["id"] != id]
        self._guardar_plantillas(plantillas)