import React, { useState } from "react";
import "../styles/Cardapio.css";

function Cardapio() {
  const categorias = {
    Espetinhos: [
      { nome: "Espetinho de Frango", preco: "R$ 8,00", imagem: "/img/frango.jpg" },
      { nome: "Espetinho de Carne", preco: "R$ 10,00", imagem: "/img/carne.jpg" },
      { nome: "Espetinho de Queijo Coalho", preco: "R$ 7,00", imagem: "/img/queijo.jpg" }
    ],
    Porções: [
      { nome: "Batata Frita", preco: "R$ 15,00", imagem: "/img/batata.jpg" },
      { nome: "Calabresa Acebolada", preco: "R$ 18,00", imagem: "/img/calabresa.jpg" }
    ],
    Bebidas: [
      { nome: "Refrigerante Lata", preco: "R$ 6,00", imagem: "/img/refri.jpg" },
      { nome: "Suco Natural", preco: "R$ 8,00", imagem: "/img/suco.jpg" },
      { nome: "Cerveja Long Neck", preco: "R$ 9,00", imagem: "/img/cerveja.jpg" }
    ]
  };

  const [categoriaAtiva, setCategoriaAtiva] = useState("Espetinhos");

  return (
    <section className="cardapio">
      <h1>📖 Cardápio</h1>

      {/* Abas para desktop */}
      <div className="tabs-cardapio">
        {Object.keys(categorias).map((cat) => (
          <button
            key={cat}
            className={`tab-btn ${categoriaAtiva === cat ? "ativo" : ""}`}
            onClick={() => setCategoriaAtiva(cat)}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Dropdown para mobile */}
      <div className="dropdown-cardapio">
        <select
          value={categoriaAtiva}
          onChange={(e) => setCategoriaAtiva(e.target.value)}
        >
          {Object.keys(categorias).map((cat) => (
            <option key={cat} value={cat}>
              {cat}
            </option>
          ))}
        </select>
      </div>

      <div className="grid-cardapio">
        {categorias[categoriaAtiva].map((item, index) => (
          <div
            className="item-cardapio fade-stagger-zoom"
            key={index}
            style={{ animationDelay: `${index * 0.15}s` }}
          >
            <img src={item.imagem} alt={item.nome} loading="lazy" />
            <div className="info-cardapio">
              <h3>{item.nome}</h3>
              <span className="preco">{item.preco}</span>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Cardapio;
