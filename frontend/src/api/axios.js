import axios from 'axios';

// Creamos una instancia de axios con la URL base del backend
// Así no tenemos que escribir http://localhost:5000 en cada petición
const api = axios.create({
  baseURL: 'http://localhost:5000/api',
});

export default api;