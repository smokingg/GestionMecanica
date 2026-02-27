import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function ProtectedRoute({ children, rolRequerido }) {
  const { usuario } = useAuth();

  // Si no hay usuario logueado va al login
  if (!usuario) {
    return <Navigate to="/" />;
  }

  // Si el rol no coincide va al login
  if (rolRequerido && usuario.rol !== rolRequerido) {
    return <Navigate to="/" />;
  }

  // Todo ok, muestra el contenido
  return children;
}

export default ProtectedRoute;