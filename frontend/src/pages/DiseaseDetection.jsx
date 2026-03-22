import React, { useState } from 'react';
import axios from 'axios';
import { Scan, UploadCloud } from 'lucide-react';

const DiseaseDetection = () => {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    if(selected) setPreview(URL.createObjectURL(selected));
    setResult(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    
    const formData = new FormData();
    formData.append('image', file);
    
    try {
      const res = await axios.post('http://127.0.0.1:5000/api/predict_disease', formData);
      setResult(res.data);
    } catch (err) {
      alert("Error analyzing image. Make sure your Python backend is running!");
    }
    setLoading(false);
  };

  return (
    <div className="form-container">
      <div style={{textAlign: 'center', marginBottom: '2rem'}}>
        <Scan size={48} color="var(--primary)" style={{marginBottom: '0.5rem'}} />
        <h2 style={{color: 'var(--primary-dark)', fontSize: '2rem', margin: '0'}}>Disease Detection AI</h2>
        <p style={{color: 'var(--text-muted)'}}>Upload a picture of a leaf for instant diagnosis.</p>
      </div>
      
      <form onSubmit={handleSubmit} style={{display: 'flex', flexDirection: 'column', gap: '1.5rem', alignItems: 'center'}}>
        
        <label style={{
            border: '2px dashed #10b981', 
            borderRadius: '16px', 
            padding: preview ? '1rem' : '3rem',
            width: '100%',
            textAlign: 'center',
            cursor: 'pointer',
            background: 'rgba(16, 185, 129, 0.05)',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '1rem'
        }}>
            {preview ? (
                <img src={preview} alt="Leaf preview" style={{maxHeight: '200px', borderRadius: '8px'}} />
            ) : (
                <>
                    <UploadCloud size={48} color="var(--primary-dark)"/>
                    <span style={{fontWeight: 600, color: 'var(--text-main)'}}>Click to upload a leaf image</span>
                </>
            )}
            <input type="file" accept="image/*" onChange={handleFileChange} style={{display: 'none'}} />
        </label>

        <button type="submit" className="submit-btn" disabled={loading || !file} style={{width: '100%'}}>
          {loading ? 'Scanning Image with Neural Network...' : 'Analyze Image'}
        </button>
      </form>

      {result && (
        <div className="result-card">
          <h3>Diagnosis Complete:</h3>
          <h2>{result.disease_detected}</h2>
          <p style={{margin: '0.5rem 0 0 0', opacity: 0.8}}>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
        </div>
      )}
    </div>
  );
};

export default DiseaseDetection;
