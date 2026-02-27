import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './components/ProtectedRoute';
import Login from './pages/Login';
import AdminDashboard from './pages/admin/Dashboard';
import MecanicoPanel from './pages/mecanico/Panel';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* Ruta pública - Login */}
          <Route path="/" element={<Login />} />

          {/* Rutas protegidas - Admin */}
          <Route
            path="/admin"
            element={
              <ProtectedRoute rolRequerido="admin">
                <AdminDashboard />
              </ProtectedRoute>
            }
          />

          {/* Rutas protegidas - Mecánico */}
          <Route
            path="/mecanico"
            element={
              <ProtectedRoute rolRequerido="mecanico">
                <MecanicoPanel />
              </ProtectedRoute>
            }
          />

          {/* Cualquier ruta desconocida redirige al login */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;