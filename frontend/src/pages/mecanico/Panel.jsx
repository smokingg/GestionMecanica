import { useAuth } from '../../context/AuthContext';
import { useNavigate } from 'react-router-dom';

function MecanicoPanel() {
  const { usuario, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <div style={{ padding: '40px', fontFamily: 'Segoe UI', backgroundColor: '#1a1a2e', minHeight: '100vh', color: 'white' }}>
      <h1 style={{ color: '#e94560' }}>Panel Mecánico 🔩</h1>
      <p>Bienvenido, <strong>{usuario?.nombre}</strong></p>
      <button
        onClick={handleLogout}
        style={{ backgroundColor: '#e94560', color: 'white', border: 'none', padding: '10px 20px', borderRadius: '8px', cursor: 'pointer' }}
      >
        Cerrar Sesión
      </button>
    </div>
  );
}

export default MecanicoPanel;