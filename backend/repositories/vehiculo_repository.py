import json
import os

class VehiculoRepository:
    def __init__(self):
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.ruta_json = os.path.join(raiz, "data", "vehiculos.json")

    def _leer_vehiculos(self):
        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar_vehiculos(self, vehiculos):
        with open(self.ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(vehiculos, archivo, indent=4, ensure_ascii=False)

    def obtener_todos(self):
        return self._leer_vehiculos()

    def obtener_por_cliente(self, cliente_id):
        vehiculos = self._leer_vehiculos()
        # Filtramos solo los vehículos que pertenecen al cliente
        return [v for v in vehiculos if v["cliente_id"] == cliente_id]

    def buscar_por_id(self, id):
        vehiculos = self._leer_vehiculos()
        for vehiculo in vehiculos:
            if vehiculo["id"] == id:
                return vehiculo
        return None

    def buscar_por_patente(self, patente):
        vehiculos = self._leer_vehiculos()
        for vehiculo in vehiculos:
            if vehiculo["patente"].upper() == patente.upper():
                return vehiculo
        return None

    def guardar(self, vehiculo_dict):
        vehiculos = self._leer_vehiculos()
        vehiculos.append(vehiculo_dict)
        self._guardar_vehiculos(vehiculos)

    def actualizar(self, vehiculo_actualizado):
        vehiculos = self._leer_vehiculos()
        for i, vehiculo in enumerate(vehiculos):
            if vehiculo["id"] == vehiculo_actualizado["id"]:
                vehiculos[i] = vehiculo_actualizado
                break
        self._guardar_vehiculos(vehiculos)