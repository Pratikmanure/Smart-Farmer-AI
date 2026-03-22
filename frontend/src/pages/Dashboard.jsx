import React from 'react';
import { Link } from 'react-router-dom';
import { Sprout, TrendingUp, Scan, CloudSun } from 'lucide-react';

const Dashboard = () => {
  return (
    <div>
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h1 style={{ fontSize: '3rem', color: 'var(--primary-dark)', marginBottom: '0.5rem' }}>
          Welcome to Smart Farmer AI
        </h1>
        <p style={{ fontSize: '1.2rem', color: 'var(--text-muted)', maxWidth: '600px', margin: '0 auto' }}>
          Your intelligent agricultural assistant. Use AI to maximize your crop yield, identify diseases, and pick the perfect crops for your soil.
        </p>
      </div>

      <div className="dashboard-grid">
        <Link to="/crop" className="feature-card">
          <div className="icon-wrapper">
            <Sprout size={48} />
          </div>
          <h2>Crop Recommendation</h2>
          <p>Input your soil metrics (Nitrogen, Phosphorous, Potassium) and current weather to find out which crop will thrive the most.</p>
        </Link>
        
        <Link to="/yield" className="feature-card">
          <div className="icon-wrapper">
            <TrendingUp size={48} />
          </div>
          <h2>Yield Prediction</h2>
          <p>Estimate how many tons per hectare your farm will produce based on localized environmental data and historical AI models.</p>
        </Link>
        
        <Link to="/disease" className="feature-card">
          <div className="icon-wrapper">
            <Scan size={48} />
          </div>
          <h2>Disease Detection</h2>
          <p>Upload a photo of a sick plant leaf. Our Computer Vision AI will instantly diagnose the illness (Apple Scab, Tomato Blight, etc).</p>
        </Link>
      </div>
    </div>
  );
};

export default Dashboard;
