import React from "react";
import Slider from "react-slick";
import { FaChevronLeft, FaChevronRight } from "react-icons/fa";
import useNavbarOffset from "./useNavbarOffset";
import "../styles/HeaderCarousel.css";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

function PrevArrow(props) {
  const { className, onClick } = props;
  return (
    <div className={className} onClick={onClick}>
      <FaChevronLeft />
    </div>
  );
}

function NextArrow(props) {
  const { className, onClick } = props;
  return (
    <div className={className} onClick={onClick}>
      <FaChevronRight />
    </div>
  );
}

function HeaderCarousel() {
  const offset = useNavbarOffset(); // hook reutilizável

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
        {/* slides aqui */}
      </Slider>
    </header>
  );
}

export default HeaderCarousel;
