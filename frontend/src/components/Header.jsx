import React from "react";
import "../styles/Header.css";

function Header() {
  return (
    <header className="header">
      <div className="header-container">
        <h1>Espetos Cia</h1>
        <p>Os melhores espetinhos da cidade, preparados com carinho e sabor.</p>
        <a href="/cardapio" className="btn-primary">Ver Cardápio</a>
      </div>
    </header>
  );
}

export default Header;
