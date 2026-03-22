import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import os

print("🍅 Generating Mock Image Data for Plant Disease Classification...")

# For image classification testing, we'll create a basic mock dataset
# 500 images of size 128x128 with 3 color channels (RGB)
num_samples = 500
image_size = (128, 128, 3)
num_classes = 3 # 0: Healthy, 1: Apple Scab, 2: Tomato Blight

X = np.random.rand(num_samples, *image_size).astype('float32') # Random noise images
y = np.random.randint(0, num_classes, num_samples) # Random labels

print("⚙️ Defining deep learning CNN (Convolutional Neural Network)...")

model = models.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=image_size),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax') # 3 classes output probabilities
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("🚀 Training the Neural Network (this will take a few seconds)...")
# Epochs = 3 (very short just to build the file structure and weights for API)
model.fit(X, y, epochs=3, batch_size=32, verbose=1)

print("✅ Disease Model trained successfully!")

models_dir = os.path.join(os.path.dirname(__file__), 'models')
os.makedirs(models_dir, exist_ok=True)
model_path = os.path.join(models_dir, 'disease_model.keras')

model.save(model_path)
print(f"💾 Keras CNN saved successfully at: {model_path}")
