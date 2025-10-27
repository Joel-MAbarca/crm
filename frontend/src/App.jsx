import { useState, useEffect } from 'react';
import './App.css'; 
import Login from './components/auth/Login';

function App() {
  return (
    <div className="crm-container">
      <h1>CRM Dashboard</h1>
      <p>API URL: {import.meta.env.VITE_API_URL}</p>
      <Login /> 
    </div>
  );
}

export default App;