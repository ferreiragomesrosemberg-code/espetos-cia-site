import React from "react";
import "../styles/Galeria.css";

function Galeria() {
  const midias = [
    { type: "image", src: "/images/espetinho1.jpg", alt: "Espetinho na brasa" },
    { type: "image", src: "/images/ambiente.jpg", alt: "Ambiente acolhedor" },
    { type: "video", src: "/videos/preparo.mp4", alt: "Preparo do espeto" },
    { type: "image", src: "/images/clientes.jpg", alt: "Clientes felizes" },
  ];

  return (
    <section className="galeria">
      <h2>Nosso Ambiente & Sabores</h2>
      <div className="galeria-grid">
        {midias.map((m, index) => (
          m.type === "image" ? (
            <img key={index} src={m.src} alt={m.alt} className="galeria-item" />
          ) : (
            <video key={index} controls className="galeria-item">
              <source src={m.src} type="video/mp4" />
              Seu navegador não suporta vídeo.
            </video>
          )
        ))}
      </div>
    </section>
  );
}

export default Galeria;
