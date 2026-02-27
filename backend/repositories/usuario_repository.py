import json
import os

class UsuarioRepository:
    def __init__(self):
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.ruta_json = os.path.join(raiz, "data", "usuarios.json")

    def _leer_usuarios(self):
        with open(self.ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar_usuarios(self, usuarios):
        with open(self.ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

    def buscar_por_usuario(self, nombre_usuario):
        usuarios = self._leer_usuarios()
        for usuario in usuarios:
            if usuario["usuario"] == nombre_usuario:
                return usuario
        return None

    def obtener_todos(self):
        return self._leer_usuarios()

    def guardar(self, usuario_dict):
        usuarios = self._leer_usuarios()
        usuarios.append(usuario_dict)
        self._guardar_usuarios(usuarios)

    def actualizar(self, usuario_actualizado):
        usuarios = self._leer_usuarios()
        for i, usuario in enumerate(usuarios):
            if usuario["id"] == usuario_actualizado["id"]:
                usuarios[i] = usuario_actualizado
                break
        self._guardar_usuarios(usuarios)