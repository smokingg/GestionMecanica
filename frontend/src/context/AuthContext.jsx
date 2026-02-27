import { createContext, useState, useContext } from 'react';

// Creamos el contexto
const AuthContext = createContext();

// Este componente envuelve toda la app y comparte el estado
export function AuthProvider({ children }) {
  const [usuario, setUsuario] = useState(null);

  const login = (datosUsuario) => {
    setUsuario(datosUsuario);
    // Guardamos en localStorage para que no se pierda al recargar
    localStorage.setItem('usuario', JSON.stringify(datosUsuario));
  };

  const logout = () => {
    setUsuario(null);
    localStorage.removeItem('usuario');
  };

  // Al cargar la app verificamos si había una sesión guardada
  const usuarioGuardado = usuario || JSON.parse(localStorage.getItem('usuario'));

  return (
    <AuthContext.Provider value={{ usuario: usuarioGuardado, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

// Hook personalizado para usar el contexto fácilmente
// En vez de escribir useContext(AuthContext) en cada componente
// solo escribimos useAuth()
export function useAuth() {
  return useContext(AuthContext);
}