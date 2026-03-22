import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import CropSuggestion from './pages/CropSuggestion';
import YieldPrediction from './pages/YieldPrediction';
import DiseaseDetection from './pages/DiseaseDetection';

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <div className="page-container">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/crop" element={<CropSuggestion />} />
            <Route path="/yield" element={<YieldPrediction />} />
            <Route path="/disease" element={<DiseaseDetection />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
