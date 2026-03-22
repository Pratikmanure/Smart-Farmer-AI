import React, { useState } from 'react';
import axios from 'axios';
import { TrendingUp } from 'lucide-react';

const YieldPrediction = () => {
  const [formData, setFormData] = useState({
    N: '', P: '', K: '', temperature: '', humidity: '', ph: '', rainfall: ''
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => setFormData({...formData, [e.target.name]: e.target.value});

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const payload = {
          N: parseFloat(formData.N), P: parseFloat(formData.P), K: parseFloat(formData.K),
          temperature: parseFloat(formData.temperature), humidity: parseFloat(formData.humidity),
          ph: parseFloat(formData.ph), rainfall: parseFloat(formData.rainfall)
      };
      
      const res = await axios.post('http://127.0.0.1:5000/api/predict_yield', payload);
      setResult(res.data.estimated_yield_tons_per_hectare);
    } catch (err) {
      alert("Error predicting yield. Make sure your Python backend is running!");
    }
    setLoading(false);
  };

  return (
    <div className="form-container">
      <div style={{textAlign: 'center', marginBottom: '2rem'}}>
        <TrendingUp size={48} color="var(--primary)" style={{marginBottom: '0.5rem'}} />
        <h2 style={{color: 'var(--primary-dark)', fontSize: '2rem', margin: '0'}}>Yield Prediction AI</h2>
        <p style={{color: 'var(--text-muted)'}}>Estimate tons per hectare based on environmental factors.</p>
      </div>
      
      <form onSubmit={handleSubmit} className="form-grid">
        <div className="form-group"><label>Nitrogen (N)</label><input type="number" step="0.01" name="N" required onChange={handleChange}/></div>
        <div className="form-group"><label>Phosphorous (P)</label><input type="number" step="0.01" name="P" required onChange={handleChange}/></div>
        <div className="form-group"><label>Potassium (K)</label><input type="number" step="0.01" name="K" required onChange={handleChange}/></div>
        <div className="form-group"><label>Soil pH level</label><input type="number" step="0.01" name="ph" required onChange={handleChange}/></div>
        <div className="form-group"><label>Temperature (°C)</label><input type="number" step="0.01" name="temperature" required onChange={handleChange}/></div>
        <div className="form-group"><label>Humidity (%)</label><input type="number" step="0.01" name="humidity" required onChange={handleChange}/></div>
        <div className="form-group"><label>Rainfall (mm)</label><input type="number" step="0.01" name="rainfall" required onChange={handleChange}/></div>
        
        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? 'Calculating...' : 'Predict Yield Volume'}
        </button>
      </form>

      {result && (
        <div className="result-card">
          <h3>Estimated Farm Yield:</h3>
          <h2>{result} Tons / Hectare 🌾</h2>
        </div>
      )}
    </div>
  );
};

export default YieldPrediction;
