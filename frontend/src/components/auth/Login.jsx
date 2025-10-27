import { useState } from 'react';
import { Form, Button, Container, Card, Alert } from 'react-bootstrap';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

// SOLUCIÓN DEFINITIVA: 
// Para evitar la advertencia de 'es2015' y asegurar que la variable se resuelva en Vite/Railway,
// creamos una función para obtener el valor dinámicamente.
const getApiUrl = () => {
  // Verificamos si import.meta está disponible (ambiente Vite)
  if (typeof import.meta !== 'undefined' && import.meta.env) {
    return import.meta.env.VITE_API_URL;
  }
  // Fallback si la sintaxis import.meta no es reconocida (aunque no debería ocurrir en un build de Vite)
  return undefined; 
};

const VITE_API_URL = getApiUrl();
const API_BASE_URL = VITE_API_URL || 'http://localhost:8000';
const LOGIN_URL = `${API_BASE_URL}/api/auth/login/`;

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // Limpiar errores anteriores
    
    // Pequeño chequeo de debug para confirmar que la URL se está usando correctamente
    console.log("Intentando iniciar sesión en:", LOGIN_URL);

    try {
      // Usar la URL dinámica
      const res = await axios.post(LOGIN_URL, {
        email,
        password
      });
      
      // Manejo de tokens y navegación
      localStorage.setItem('access_token', res.data.access);
      navigate('/dashboard');
    } catch (err) {
      // Manejo de errores más específico, capturando el detalle del backend
      const message = err.response?.data?.detail 
                      ? `Error: ${err.response.data.detail}` 
                      : 'Credenciales inválidas o error de conexión. Verifique la URL de la API.';
      setError(message);
      console.error("Error de login:", err);
    }
  };

  return (
    <Container className="d-flex justify-content-center align-items-center min-vh-100">
      <Card style={{ width: '25rem' }} className="shadow">
        <Card.Body className="p-5">
          <h3 className="text-center mb-4">CRM GDGROUP</h3>
          {error && <Alert variant="danger">{error}</Alert>}
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                placeholder="tu@email.com"
              />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Contraseña</Form.Label>
              <Form.Control
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </Form.Group>
            <Button variant="success" type="submit" className="w-100">
              Iniciar Sesión
            </Button>
          </Form>
        </Card.Body>
      </Card>
    </Container>
  );
}
