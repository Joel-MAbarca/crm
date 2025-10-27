import { useState, useEffect } from 'react';
import './App.css'; 
import ClientList from './components/ClientList'; 

function App() {
  return (
    <div className="crm-container">
      <h1>CRM Dashboard</h1>
      <p>API URL: {import.meta.env.VITE_API_URL}</p>
      <ClientList /> 
    </div>
  );
}

export default App;