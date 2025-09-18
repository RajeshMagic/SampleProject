"""
TensorFlow - Introduction and Simple Neural Network Example
This script demonstrates:
1. Loading and preprocessing the MNIST dataset
2. Building a simple neural network using TensorFlow's Keras API
3. Training the model with detailed console output
4. Evaluating the model on test data
5. Visualizing sample predictions
"""

# ------------------------------
# Step 1: Import required modules
# ------------------------------
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np

print("Step 1: Imported TensorFlow and other required libraries.\n")

# ------------------------------
# Step 2: Load the MNIST dataset
# ------------------------------
print("Step 2: Loading MNIST dataset...")
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(f"Training data shape: {train_images.shape}, Training labels shape: {train_labels.shape}")
print(f"Test data shape: {test_images.shape}, Test labels shape: {test_labels.shape}")
print("Important Note: MNIST dataset contains 28x28 grayscale images of digits 0-9.\n")

# ------------------------------
# Step 3: Preprocess the data
# ------------------------------
print("Step 3: Preprocessing data (flatten and normalize)...")
# Flatten the 28x28 images into vectors of size 784
train_images = train_images.reshape((train_images.shape[0], 28 * 28)).astype('float32') / 255
test_images = test_images.reshape((test_images.shape[0], 28 * 28)).astype('float32') / 255
print(f"Preprocessed training data shape: {train_images.shape}")
print(f"Preprocessed test data shape: {test_images.shape}")
print("Important Note: Pixel values normalized to range [0,1] for faster convergence.\n")

# ------------------------------
# Step 4: Build the neural network
# ------------------------------
print("Step 4: Building a simple neural network with Keras Sequential API...")
model = Sequential([
    Dense(128, activation='relu', input_shape=(28 * 28,)),  # Hidden layer
    Dense(10, activation='softmax')                        # Output layer for 10 classes
])
model.summary()
print("Important Note: ReLU activation in hidden layers helps learn non-linear features, softmax outputs probabilities.\n")

# ------------------------------
# Step 5: Compile the model
# ------------------------------
print("Step 5: Compiling the model with Adam optimizer and sparse categorical crossentropy...")
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print("Important Note: Sparse categorical crossentropy is used when labels are integers, not one-hot vectors.\n")

# ------------------------------
# Step 6: Train the model
# ------------------------------
print("Step 6: Training the model for 5 epochs...")
history = model.fit(train_images, train_labels, epochs=5, validation_split=0.1)
print("Important Note: Training accuracy and validation accuracy printed per epoch.\n")

# ------------------------------
# Step 7: Evaluate the model
# ------------------------------
print("Step 7: Evaluating the model on test data...")
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.4f}")
print(f"Test loss: {test_loss:.4f}")
print("Important Note: High test accuracy indicates good generalization.\n")

# ------------------------------
# Step 8: Visualize sample predictions
# ------------------------------
print("Step 8: Visualizing sample predictions...")
sample_indices = np.random.choice(len(test_images), size=5, replace=False)
sample_images = test_images[sample_indices]
sample_labels = test_labels[sample_indices]
predictions = model.predict(sample_images)

plt.figure(figsize=(10,4))
for i, idx in enumerate(sample_indices):
    plt.subplot(1, 5, i+1)
    plt.imshow(sample_images[i].reshape(28,28), cmap='gray')
    plt.title(f"True: {sample_labels[i]}\nPred: {np.argmax(predictions[i])}")
    plt.axis('off')
plt.show()
print("Important Note: Predictions show the model's ability to classify unseen images correctly.\n")

# ------------------------------
# Step 9: Plot training history
# ------------------------------
print("Step 9: Plotting training and validation accuracy over epochs...")
plt.figure(figsize=(8,5))
plt.plot(history.history['accuracy'], label='Train Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', marker='x')
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Training vs Validation Accuracy")
plt.legend()
plt.grid(True)
plt.show()
print("Important Note: Visualizing training history helps detect overfitting or underfitting.\n")

# ------------------------------
# Step 10: Summary of key points
# ------------------------------
print("Step 10: Key Points Learned")
print("""
1. TensorFlow allows building neural networks easily using Keras API.
2. MNIST dataset contains 28x28 grayscale digit images; normalization improves training speed.
3. Simple dense network with ReLU and softmax can classify digits effectively.
4. Validation during training is important to monitor model generalization.
5. Visualization of predictions and training history helps in understanding model behavior.
""")
