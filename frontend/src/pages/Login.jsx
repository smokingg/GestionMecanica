import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import api from '../api/axios';

function Login() {
  const [usuario, setUsuario] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [cargando, setCargando] = useState(false);

  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setCargando(true);
    setError('');

    try {
      const respuesta = await api.post('/auth/login', { usuario, password });

      if (respuesta.data.ok) {
        login(respuesta.data.usuario);
        // Redirigimos según el rol
        if (respuesta.data.usuario.rol === 'admin') {
          navigate('/admin');
        } else {
          navigate('/mecanico');
        }
      }
    } catch (err) {
      // El backend devuelve 401 cuando las credenciales son incorrectas
      setError(err.response?.data?.mensaje || 'Error al conectar con el servidor');
    } finally {
      // finally siempre se ejecuta, haya error o no
      setCargando(false);
    }
  };

  return (
    <div style={estilos.contenedor}>
      <div style={estilos.tarjeta}>

        {/* Encabezado */}
        <div style={estilos.encabezado}>
          <div style={estilos.icono}>🔧</div>
          <h1 style={estilos.titulo}>Taller Mecánico</h1>
          <p style={estilos.subtitulo}>Sistema de Gestión</p>
        </div>

        {/* Formulario */}
        <form onSubmit={handleLogin} style={estilos.formulario}>
          <div style={estilos.campo}>
            <label style={estilos.label}>Usuario</label>
            <input
              style={estilos.input}
              type="text"
              value={usuario}
              onChange={(e) => setUsuario(e.target.value)}
              placeholder="Ingresa tu usuario"
              required
            />
          </div>

          <div style={estilos.campo}>
            <label style={estilos.label}>Contraseña</label>
            <input
              style={estilos.input}
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Ingresa tu contraseña"
              required
            />
          </div>

          {/* Mensaje de error */}
          {error && <div style={estilos.error}>{error}</div>}

          <button
            style={cargando ? estilos.botonCargando : estilos.boton}
            type="submit"
            disabled={cargando}
          >
            {cargando ? 'Ingresando...' : 'Ingresar'}
          </button>
        </form>
      </div>
    </div>
  );
}

const estilos = {
  contenedor: {
    minHeight: '100vh',
    backgroundColor: '#1a1a2e',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontFamily: "'Segoe UI', sans-serif",
  },
  tarjeta: {
    backgroundColor: '#16213e',
    borderRadius: '16px',
    padding: '48px',
    width: '100%',
    maxWidth: '420px',
    boxShadow: '0 20px 60px rgba(0,0,0,0.5)',
    border: '1px solid #0f3460',
  },
  encabezado: {
    textAlign: 'center',
    marginBottom: '36px',
  },
  icono: {
    fontSize: '48px',
    marginBottom: '12px',
  },
  titulo: {
    color: '#e94560',
    fontSize: '28px',
    fontWeight: '700',
    margin: '0 0 8px 0',
  },
  subtitulo: {
    color: '#a0a0b0',
    fontSize: '14px',
    margin: 0,
  },
  formulario: {
    display: 'flex',
    flexDirection: 'column',
    gap: '20px',
  },
  campo: {
    display: 'flex',
    flexDirection: 'column',
    gap: '8px',
  },
  label: {
    color: '#a0a0b0',
    fontSize: '14px',
    fontWeight: '500',
  },
  input: {
    backgroundColor: '#0f3460',
    border: '1px solid #1a4a7a',
    borderRadius: '8px',
    padding: '12px 16px',
    color: '#ffffff',
    fontSize: '15px',
    outline: 'none',
  },
  boton: {
    backgroundColor: '#e94560',
    color: '#ffffff',
    border: 'none',
    borderRadius: '8px',
    padding: '14px',
    fontSize: '16px',
    fontWeight: '600',
    cursor: 'pointer',
    marginTop: '8px',
  },
  botonCargando: {
    backgroundColor: '#a0a0b0',
    color: '#ffffff',
    border: 'none',
    borderRadius: '8px',
    padding: '14px',
    fontSize: '16px',
    fontWeight: '600',
    cursor: 'not-allowed',
    marginTop: '8px',
  },
  error: {
    backgroundColor: '#3d1515',
    color: '#ff6b6b',
    padding: '12px',
    borderRadius: '8px',
    fontSize: '14px',
    textAlign: 'center',
  },
};

export default Login;