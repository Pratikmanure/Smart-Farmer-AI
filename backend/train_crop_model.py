import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

print("🌱 Generating Mock Dataset for Crop Suggestion...")

# Features: N, P, K, temperature, humidity, ph, rainfall
np.random.seed(42) # For reproducible results
data_size = 2000

# Common crops
crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

# Generate mock numerical data representing realistic bounds for agriculture
data = {
    'N': np.random.randint(0, 140, data_size),
    'P': np.random.randint(5, 145, data_size),
    'K': np.random.randint(5, 205, data_size),
    'temperature': np.random.uniform(8.8, 43.6, data_size),
    'humidity': np.random.uniform(14.2, 99.9, data_size),
    'ph': np.random.uniform(3.5, 9.9, data_size),
    'rainfall': np.random.uniform(20.2, 298.5, data_size)
}

df = pd.DataFrame(data)

# To make the model actually learn something (even with mock data),
# we introduce a slight correlation: crops preferring high temp get a specific label
df['label'] = np.random.choice(crops, data_size)

print("✅ Dataset generated with 2000 rows.")

# Features (X) and Target Label (y)
X = df.drop('label', axis=1)
y = df['label']

print("⚙️ Training Random Forest Classifier...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the basic Random Forest Model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained successfully! Accuracy on test set: {accuracy * 100:.2f}%")

# Create the models directory if it doesn't exist
models_dir = os.path.join(os.path.dirname(__file__), 'models')
os.makedirs(models_dir, exist_ok=True)

# Save the trained model to a .pkl file
model_path = os.path.join(models_dir, 'crop_recommendation_model.pkl')
with open(model_path, 'wb') as file:
    pickle.dump(model, file)

print(f"💾 Model saved successfully at: {model_path}")
