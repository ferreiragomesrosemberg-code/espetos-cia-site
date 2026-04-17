import React from "react";
import Slider from "react-slick";
import "../styles/ProdutosDestaque.css";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

function ProdutosDestaque() {
  const produtos = [
    { nome: "Espetinhos", preco: "R$ 8,00", imagem: "/img/espetos.jpg", badge: "promo" },
    { nome: "Porções", preco: "R$ 15,00", imagem: "/img/porcoes.jpg", badge: "vendido" },
    { nome: "Lanches", preco: "R$ 12,00", imagem: "/img/lanches.jpg", badge: "novo" },
    { nome: "Caldos", preco: "R$ 10,00", imagem: "/img/caldos.jpg" }
  ];

  const settings = {
    dots: true,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 4000,
    speed: 600,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
      { breakpoint: 992, settings: { slidesToShow: 2 } },
      { breakpoint: 600, settings: { slidesToShow: 1 } }
    ]
  };

  return (
    <section className="produtos-destaque">
      <h2>🍢 Produtos em Destaque</h2>
      <Slider {...settings} className="produtos-carousel">
        {produtos.map((item, index) => (
          <div className="card-produto" key={index}>
            <img src={item.imagem} alt={item.nome} loading="lazy" />
            {/* Badge condicional */}
            {item.badge === "promo" && <span className="badge badge-promo">🔥 Promoção</span>}
            {item.badge === "novo" && <span className="badge badge-novo">✨ Novo</span>}
            {item.badge === "vendido" && <span className="badge badge-vendido">🏆 Mais vendido</span>}
            
            <h3>{item.nome}</h3>
            <p>{item.preco}</p>
            <button className="btn-comprar">Comprar</button>
          </div>
        ))}
      </Slider>
    </section>
  );
}

export default ProdutosDestaque;
