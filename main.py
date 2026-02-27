import sys
import os

# Agregamos la carpeta backend al path de Python
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))

from backend.app import create_app

app = create_app()

if __name__ == "__main__":
    print("🔧 Taller Mecánico - Sistema iniciando...")
    print("📡 Servidor corriendo en http://localhost:5000")
    print("✅ Presiona CTRL+C para detener")
    # debug=True hace que el servidor se reinicie automáticamente
    # cada vez que guardas cambios en el código
    app.run(debug=True, port=5000)