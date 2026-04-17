import React from "react";
import HeaderCarousel from "../components/HeaderCarousel";
import ProdutosDestaque from "../components/ProdutosDestaque";
import Depoimentos from "../components/Depoimentos";
import Banners from "../components/Banners";
import Galeria from "../components/Galeria";

function Home() {
  const bannersHome = [
    { text: "🖼️ BANNER HEINEKEN" },
    { text: "🖼️ BANNER MERCADO LOCAL" },
    { text: "🖼️ BANNER RESTAURANTE" },
    { text: "🖼️ BANNER EVENTO DA CIDADE" },
  ];

  return (
    <div>
      <HeaderCarousel />
      <ProdutosDestaque />

      {/* Botões de navegação para páginas principais */}
      <div className="home-links">
        <button onClick={() => window.location.href="/cardapio"}>🍖 Veja o Cardápio</button>
        <button onClick={() => window.location.href="/promocoes"}>🔥 Promoções</button>
        <button onClick={() => window.location.href="/contato"}>📞 Contato</button>
      </div>

      <Banners banners={bannersHome} />

      {/* Galeria de fotos e vídeos */}
      <Galeria />

      <Depoimentos />
    </div>
  );
}

export default Home;
