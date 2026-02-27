import json
import os

class MecanicoRepository:
    def __init__(self):
        # Mismo patrón que usuario_repository
        # 3 dirname para llegar a la raíz Mecanica/
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.ruta_json = os.path.join(raiz, "data", "mecanicos.json")

    def _leer_mecanicos(self):
        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar_mecanicos(self, mecanicos):
        with open(self.ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(mecanicos, archivo, indent=4, ensure_ascii=False)

    def obtener_todos(self):
        return self._leer_mecanicos()

    def obtener_activos(self):
        mecanicos = self._leer_mecanicos()
        # Filtramos solo los que tienen activo = True
        # Esta sintaxis se llama "list comprehension"
        # Es una forma corta de recorrer una lista y filtrar
        return [m for m in mecanicos if m["activo"]]

    def buscar_por_id(self, id):
        mecanicos = self._leer_mecanicos()
        for mecanico in mecanicos:
            if mecanico["id"] == id:
                return mecanico
        return None

    def buscar_por_usuario(self, nombre_usuario):
        mecanicos = self._leer_mecanicos()
        for mecanico in mecanicos:
            if mecanico["usuario"] == nombre_usuario:
                return mecanico
        return None

    def guardar(self, mecanico_dict):
        mecanicos = self._leer_mecanicos()
        mecanicos.append(mecanico_dict)
        self._guardar_mecanicos(mecanicos)

    def actualizar(self, mecanico_actualizado):
        mecanicos = self._leer_mecanicos()
        for i, mecanico in enumerate(mecanicos):
            if mecanico["id"] == mecanico_actualizado["id"]:
                mecanicos[i] = mecanico_actualizado
                break
        self._guardar_mecanicos(mecanicos)