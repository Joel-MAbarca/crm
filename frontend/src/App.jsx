// App.js
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container, Navbar, Nav } from 'react-bootstrap';
import axios from 'axios';
import { useEffect, useState } from 'react';
import ComunasCRUD from './components/crm/ComunasCRUD';
import CategoriasCRUD from './components/crm/CategoriasCRUD';
// ... imports para otros components

function App() {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    // Fetch weather (de tu JS en base.html, adapta API key segura via env)
    axios.get('https://api.openweathermap.org/data/2.5/weather?q=Las%20Condes,CL&appid=YOUR_API_KEY&units=metric')
      .then(res => setWeather(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <Router>
      <Navbar bg="light" expand="lg" sticky="top" className="glass-effect"> {/* Añade custom CSS para glass */}
        <Container>
          <Navbar.Brand href="/">CRM GDGROUP</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/admin/comunas">Comunas</Nav.Link>
            <Nav.Link href="/admin/categorias">Categorias</Nav.Link>
            {/* Menús de base.html */}
          </Nav>
          {weather && <div>Clima: {weather.main.temp}°C</div>} {/* Expande como en tu HTML */}
        </Container>
      </Navbar>
      <Container className="mt-4">
        <Routes>
          <Route path="/admin/comunas" element={<ComunasCRUD />} />
          <Route path="/admin/categorias" element={<CategoriasCRUD />} />
          <Route path="/buscar-lead" element={<BuscarLead />} />
          {/* Rutas para otros */}
        </Routes>
      </Container>
    </Router>
  );
}

export default App;