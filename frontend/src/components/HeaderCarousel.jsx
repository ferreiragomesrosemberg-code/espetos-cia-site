import React, { useEffect, useState } from "react";
import Slider from "react-slick";
import { FaChevronLeft, FaChevronRight } from "react-icons/fa";
import "../styles/HeaderCarousel.css";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

function PrevArrow(props) {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{ ...style, display: "block", zIndex: 10 }}
      onClick={onClick}
      aria-label="Slide anterior"
    >
      <FaChevronLeft />
    </div>
  );
}

function NextArrow(props) {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{ ...style, display: "block", zIndex: 10 }}
      onClick={onClick}
      aria-label="Próximo slide"
    >
      <FaChevronRight />
    </div>
  );
}

function HeaderCarousel() {
  const [offset, setOffset] = useState(0);

  useEffect(() => {
    const navbar = document.querySelector(".navbar");
    if (navbar) {
      setOffset(navbar.offsetHeight);
    }
  }, []);

  const settings = {
    dots: true,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 5000,
    speed: 800,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    nextArrow: <NextArrow />,
    prevArrow: <PrevArrow />
  };

  return (
    <header className="header-carousel" style={{ marginTop: offset }}>
      <Slider {...settings}>
        <div className="slide">
          <img src="/img/slide-01.jpg" alt="Slide 1" />
          <div className="overlay">
            <h2>Espetos & Cia</h2>
            <p>Cerveja gelada e espetinho na brasa</p>
            <a href="#cardapio" className="btn">Ver Cardápio</a>
          </div>
        </div>
        <div className="slide">
          <img src="/img/slide-02.jpg" alt="Slide 2" />
          <div className="overlay">
            <h2>Promoções da Semana</h2>
            <p>Espetinho de frango por apenas R$7,00</p>
            <a href="#promocoes" className="btn">Confira</a>
          </div>
        </div>
        <div className="slide">
          <img src="/img/slide-03.jpg" alt="Slide 3" />
          <div className="overlay">
            <h2>Venha nos visitar</h2>
            <p>Av. Marechal Rondon nº2719 - Bela Vista</p>
            <a href="#contato" className="btn">Contato</a>
          </div>
        </div>
      </Slider>
    </header>
  );
}

export default HeaderCarousel;
