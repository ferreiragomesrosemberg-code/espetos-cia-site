import React, { useEffect, useState } from "react";
import Slider from "react-slick";
import { FaChevronLeft, FaChevronRight } from "react-icons/fa";
import "../styles/Depoimentos.css";

function PrevArrow(props) {
  const { className, onClick } = props;
  return (
    <div className={`${className} custom-arrow prev`} onClick={onClick}>
      <FaChevronLeft />
    </div>
  );
}

function NextArrow(props) {
  const { className, onClick } = props;
  return (
    <div className={`${className} custom-arrow next`} onClick={onClick}>
      <FaChevronRight />
    </div>
  );
}

function Depoimentos() {
  const [fadeInCards, setFadeInCards] = useState([]);

  const depoimentos = [
    {
      nome: "Maria Silva",
      comentario: "Os espetinhos são deliciosos e o atendimento é excelente!",
      imagem: "https://randomuser.me/api/portraits/women/44.jpg"
    },
    {
      nome: "João Pereira",
      comentario: "Sempre volto porque a qualidade é incrível e os preços são justos.",
      imagem: "https://randomuser.me/api/portraits/men/46.jpg"
    },
    {
      nome: "Ana Souza",
      comentario: "Ambiente agradável e espetinhos bem temperados. Recomendo!",
      imagem: "https://randomuser.me/api/portraits/women/65.jpg"
    },
    {
      nome: "Carlos Mendes",
      comentario: "Melhor churrasco da cidade, sem dúvidas!",
      imagem: "https://randomuser.me/api/portraits/men/32.jpg"
    },
    {
      nome: "Fernanda Lima",
      comentario: "Espetinhos bem servidos e saborosos, virei cliente fiel.",
      imagem: "https://randomuser.me/api/portraits/women/22.jpg"
    }
  ];

  useEffect(() => {
    depoimentos.forEach((_, i) => {
      setTimeout(() => {
        setFadeInCards(prev => [...prev, i]);
      }, i * 300);
    });
  }, []);

  const settings = {
    dots: true,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 5000,
    speed: 800,
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true, // ativa setas
    nextArrow: <NextArrow />,
    prevArrow: <PrevArrow />,
    responsive: [
      { breakpoint: 1024, settings: { slidesToShow: 2 } },
      { breakpoint: 768, settings: { slidesToShow: 1 } }
    ]
  };

  return (
    <section className="depoimentos">
      <h2>💬 Depoimentos de Clientes</h2>
      <Slider {...settings}>
        {depoimentos.map((item, index) => (
          <div
            className={`card-depoimento ${
              fadeInCards.includes(index) ? "fade-in" : ""
            }`}
            key={index}
          >
            <img src={item.imagem} alt={item.nome} />
            <p>"{item.comentario}"</p>
            <h4>- {item.nome}</h4>
          </div>
        ))}
      </Slider>
    </section>
  );
}

export default Depoimentos;
