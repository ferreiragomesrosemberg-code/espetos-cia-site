import React from "react";
import "../styles/ProdutosDestaque.css";

function ProdutosDestaque() {
  const produtos = [
    {
      nome: "Espetinhos",
      preco: "R$ 8,00",
      imagem: "/img/espetos.jpg"
    },
    {
      nome: "Porções",
      preco: "R$ 15,00",
      imagem: "/img/porcoes.jpg"
    },
    {
      nome: "Lanches",
      preco: "R$ 12,00",
      imagem: "/img/lanches.jpg"
    },
    {
      nome: "Caldos",
      preco: "R$ 10,00",
      imagem: "/img/caldos.jpg"
    }
  ];

  return (
    <section className="produtos-destaque">
      <h2>🍢 Produtos em Destaque</h2>
      <div className="produtos-grid">
        {produtos.map((item, index) => (
          <div className="card-produto" key={index}>
            {/* Lazy loading nas imagens */}
            <img src={item.imagem} alt={item.nome} loading="lazy" />
            <h3>{item.nome}</h3>
            <p>{item.preco}</p>
            <button className="btn-comprar">Comprar</button>
          </div>
        ))}
      </div>
    </section>
  );
}

export default ProdutosDestaque;
