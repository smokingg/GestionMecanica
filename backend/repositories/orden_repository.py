import json
import os

class OrdenRepository:
    def __init__(self):
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.ruta_json = os.path.join(raiz, "data", "ordenes.json")

    def _leer_ordenes(self):
        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar_ordenes(self, ordenes):
        with open(self.ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(ordenes, archivo, indent=4, ensure_ascii=False)

    def obtener_todas(self):
        return self._leer_ordenes()

    def obtener_por_mecanico(self, mecanico_id):
        ordenes = self._leer_ordenes()
        return [o for o in ordenes if o["mecanico_id"] == mecanico_id]

    def obtener_por_fecha(self, fecha):
        ordenes = self._leer_ordenes()
        return [o for o in ordenes if o["fecha_ingreso"] == fecha]

    def obtener_por_mecanico_y_fecha(self, mecanico_id, fecha):
        ordenes = self._leer_ordenes()
        return [o for o in ordenes
                if o["mecanico_id"] == mecanico_id
                and o["fecha_ingreso"] == fecha]

    def buscar_por_id(self, id):
        ordenes = self._leer_ordenes()
        for orden in ordenes:
            if orden["id"] == id:
                return orden
        return None

    def guardar(self, orden_dict):
        ordenes = self._leer_ordenes()
        ordenes.append(orden_dict)
        self._guardar_ordenes(ordenes)

    def actualizar(self, orden_actualizada):
        ordenes = self._leer_ordenes()
        for i, orden in enumerate(ordenes):
            if orden["id"] == orden_actualizada["id"]:
                ordenes[i] = orden_actualizada
                break
        self._guardar_ordenes(ordenes)