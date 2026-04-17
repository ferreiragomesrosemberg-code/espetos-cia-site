import React from "react";
import "../styles/Footer.css";
import { FaFacebook, FaInstagram, FaWhatsapp, FaMapMarkedAlt } from "react-icons/fa";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <p>© {new Date().getFullYear()} Espetos Cia - Todos os direitos reservados</p>
        
        <ul className="footer-links">
          <li><a href="/">Home</a></li>
          <li><a href="/cardapio">Cardápio</a></li>
          <li><a href="/promocoes">Promoções</a></li>
          <li><a href="/contato">Contato</a></li>
        </ul>

        <div className="social-icons">
          <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
            <FaFacebook />
          </a>
          <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">
            <FaInstagram />
          </a>
          <a href="https://wa.me/5565999999999" target="_blank" rel="noopener noreferrer">
            <FaWhatsapp />
          </a>
        </div>

        <div className="footer-contact">
          <p>📞 Telefone: (65) 99999-9999</p>
          <p>📍 Endereço: Av. Principal, 123 - Pontes e Lacerda/MT</p>
          <p>🕒 Funcionamento: Seg a Dom - 18h às 00h</p>
        </div>

        <div className="footer-map">
          <iframe
            title="Mapa Espetos Cia"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3836.123456789!2d-59.335!3d-15.221!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x939d123456789%3A0xabcdef123456789!2sPontes%20e%20Lacerda%2C%20MT!5e0!3m2!1spt-BR!2sbr!4v1681234567890!5m2!1spt-BR!2sbr"
            width="100%"
            height="250"
            style={{ border: 0 }}
            allowFullScreen=""
            loading="lazy"
          ></iframe>
        </div>

        {/* Botão de rota rápida */}
        <div className="footer-route">
          <a
            href="https://www.google.com/maps/dir/?api=1&destination=Av.+Principal,+123,+Pontes+e+Lacerda,+MT"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-route"
          >
            <FaMapMarkedAlt /> Traçar Rota
          </a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
