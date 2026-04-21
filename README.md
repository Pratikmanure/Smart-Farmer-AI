# 🚜 Smart Farmer AI Platform

A premium, full-stack agricultural decision-support application utilizing Machine Learning and Computer Vision to help farmers make data-driven decisions.

## 🌟 Features

* **🌱 Crop Suggestion (Classification):** Analyzes soil conditions (Nitrogen, Phosphorous, Potassium, pH) and weather parameters (Temperature, Humidity, Rainfall) using a Random Forest Classifier to recommend the optimal crop.
* **📈 Yield Prediction (Regression):** Utilizes a Random Forest Regressor to estimate the crop yield (in Tons per Hectare) based on complex environmental input parameters.
* **🩺 Plant Disease Detection (Computer Vision):** Implements a custom Convolutional Neural Network (CNN) to analyze uploaded images of plant leaves. The backend utilizes OpenCV to reshape images into 128x128x3 mathematical tensors to identify specific diseases.

## 🛠️ Tech Stack

* **Frontend:** React.js, Vite, React Router, Axios, Lucide-React
* **UI/UX:** Custom modern Glassmorphism architecture (`backdrop-filter`)
* **Backend:** Python, Flask, Flask-CORS
* **Machine Learning:** Scikit-Learn, TensorFlow, Keras, OpenCV (`cv2`), Pandas, NumPy

## 🚀 How to Run Locally

You will need two separate terminal windows to run the React frontend and the Python backend simultaneously.

### 1. Start the Machine Learning Backend
```powershell
cd smart_farmer_assistant/backend
# Activate your virtual environment
.\venv\Scripts\Activate
# Install required libraries (only needed once)
pip install -r requirements.txt
# Turn on the AI Engine
python app.py
```
*The backend API will run steadily on `http://localhost:5000`*

### 2. Start the React User Interface
```powershell
cd smart_farmer_assistant/frontend
# Install Node dependencies (only needed once)
npm install
# Boot up the Vite server
npm run dev
```
*Hold `Ctrl` and click the generated `http://localhost:5173` link to view the app!*

## 📡 Core API Routes

* `POST /api/predict_crop`: Accepts serialized JSON payload of tabular environmental features.
* `POST /api/predict_yield`: Accepts serialized JSON payload of tabular environmental features.
* `POST /api/predict_disease`: Accepts `multipart/form-data` raw image uploads for Computer Vision processing.

---
*Built from scratch for agricultural machine learning integration.*
