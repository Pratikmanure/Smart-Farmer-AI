from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import tensorflow as tf
import cv2
import os

app = Flask(__name__)
# Enable CORS so our React frontend on port 5173 can talk to this port 5000 API
CORS(app)

# ---------------------------------------------
# 1. LOAD THE MACHINE LEARNING MODELS INTO MEMORY
# ---------------------------------------------
models_dir = os.path.join(os.path.dirname(__file__), 'models')
try:
    with open(os.path.join(models_dir, 'crop_recommendation_model.pkl'), 'rb') as f:
        crop_model = pickle.load(f)
        
    with open(os.path.join(models_dir, 'crop_yield_model.pkl'), 'rb') as f:
        yield_model = pickle.load(f)
        
    disease_model = tf.keras.models.load_model(os.path.join(models_dir, 'disease_model.keras'))
    print("\n✅ All 3 AI Models Loaded Successfully!\n")
except Exception as e:
    print(f"\n⚠️ Error loading models: {e}\n")


# ---------------------------------------------
# 2. DEFINE THE API ENDPOINTS (ROUTES)
# ---------------------------------------------
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "success", "message": "Smart Farmer AI is running!"})

@app.route('/api/predict_crop', methods=['POST'])
def predict_crop():
    """Takes Soil and Weather JSON array -> Returns Recommended Crop String"""
    try:
        data = request.json
        features = np.array([[
            data['N'], data['P'], data['K'], 
            data['temperature'], data['humidity'], 
            data['ph'], data['rainfall']
        ]])
        prediction = crop_model.predict(features)[0]
        return jsonify({"recommended_crop": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/predict_yield', methods=['POST'])
def predict_yield():
    """Takes Soil and Weather JSON array -> Returns Estimated Yield Number"""
    try:
        data = request.json
        features = np.array([[
            data['N'], data['P'], data['K'], 
            data['temperature'], data['humidity'], 
            data['ph'], data['rainfall']
        ]])
        prediction = yield_model.predict(features)[0]
        return jsonify({"estimated_yield_tons_per_hectare": round(prediction, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/predict_disease', methods=['POST'])
def predict_disease():
    """Takes an Image File Upload -> Returns Disease Class String"""
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400
        
        file = request.files['image']
        image_bytes = file.read()
        
        # Open image bytes with OpenCV and resize to 128x128 as expected by our CNN model
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert to standard RGB
        img = cv2.resize(img, (128, 128))
        
        # Normalize pixel values and prepare the batch shape for Keras (1, 128, 128, 3)
        img_array = img.astype('float32') / 255.0
        img_array = np.expand_dims(img_array, axis=0) 
        
        predictions = disease_model.predict(img_array)
        class_idx = np.argmax(predictions[0])
        classes = ["Healthy", "Apple Scab", "Tomato Blight"]
        
        return jsonify({
            "disease_detected": classes[class_idx],
            "confidence": float(np.max(predictions[0]))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Start Server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
