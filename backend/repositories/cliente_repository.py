import json
import os

class ClienteRepository:
    def __init__(self):
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.ruta_json = os.path.join(raiz, "data", "clientes.json")

    def _leer_clientes(self):
        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar_clientes(self, clientes):
        with open(self.ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(clientes, archivo, indent=4, ensure_ascii=False)

    def obtener_todos(self):
        return self._leer_clientes()

    def buscar_por_id(self, id):
        clientes = self._leer_clientes()
        for cliente in clientes:
            if cliente["id"] == id:
                return cliente
        return None

    def buscar_por_rut(self, rut):
        clientes = self._leer_clientes()
        for cliente in clientes:
            if cliente["rut"] == rut:
                return cliente
        return None

    def guardar(self, cliente_dict):
        clientes = self._leer_clientes()
        clientes.append(cliente_dict)
        self._guardar_clientes(clientes)

    def actualizar(self, cliente_actualizado):
        clientes = self._leer_clientes()
        for i, cliente in enumerate(clientes):
            if cliente["id"] == cliente_actualizado["id"]:
                clientes[i] = cliente_actualizado
                break
        self._guardar_clientes(clientes)