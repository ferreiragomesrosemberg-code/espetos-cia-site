import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <h2 className="logo">Espetos Cia</h2>
        <button 
          className="menu-toggle" 
          onClick={() => setOpen(!open)} 
          aria-label="Abrir menu de navegação"
        >
          ☰
        </button>
        <ul className={`nav-links ${open ? "open" : ""}`}>
          <li><Link to="/" onClick={() => setOpen(false)}>Home</Link></li>
          <li><Link to="/cardapio" onClick={() => setOpen(false)}>Cardápio</Link></li>
          <li><Link to="/promocoes" onClick={() => setOpen(false)}>Promoções</Link></li>
          <li><Link to="/contato" onClick={() => setOpen(false)}>Contato</Link></li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
