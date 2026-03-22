import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Sprout } from 'lucide-react';

const Navbar = () => {
  const location = useLocation();
  
  const navLinks = [
    { name: 'Dashboard', path: '/' },
    { name: 'Crop Recommendation', path: '/crop' },
    { name: 'Yield Prediction', path: '/yield' },
    { name: 'Disease Detection', path: '/disease' }
  ];

  return (
    <nav className="navbar">
      <Link to="/" className="nav-brand">
        <Sprout size={28} />
        Smart Farmer AI
      </Link>
      <div className="nav-links">
        {navLinks.map((link) => (
          <Link 
            key={link.path} 
            to={link.path}
            className={`nav-link ${location.pathname === link.path ? 'active' : ''}`}
          >
            {link.name}
          </Link>
        ))}
      </div>
    </nav>
  );
};

export default Navbar;
