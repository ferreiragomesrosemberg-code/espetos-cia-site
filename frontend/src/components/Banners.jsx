import React from "react";
import "../styles/Banners.css";

function Banners({ banners }) {
  return (
    <aside className="banners-lateral">
      {banners.map((banner, index) => (
        <div key={index} className="banner placeholder">
          {banner.text ? banner.text : <img src={banner.img} alt={banner.alt} />}
        </div>
      ))}
    </aside>
  );
}

export default Banners;
