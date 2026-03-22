import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

print("🌾 Generating Mock Dataset for Crop Yield Prediction...")

np.random.seed(42)
data_size = 2000
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

# Yield targets (tons/hectare) usually correlate with inputs
df['yield'] = (df['N']*0.1 + df['P']*0.05 + df['K']*0.08 + df['rainfall']*0.02 + np.random.normal(0, 2, data_size))

X = df.drop('yield', axis=1)
y = df['yield']

print("⚙️ Training Random Forest Regressor for Yield...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# For regression, we use R2 score instead of accuracy
r2_score = model.score(X_test, y_test)
print(f"✅ Yield Model trained successfully! R-squared score: {r2_score:.4f}")

models_dir = os.path.join(os.path.dirname(__file__), 'models')
os.makedirs(models_dir, exist_ok=True)
model_path = os.path.join(models_dir, 'crop_yield_model.pkl')

with open(model_path, 'wb') as file:
    pickle.dump(model, file)

print(f"💾 Yield Model saved successfully at: {model_path}")
