import time
import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
mnist = datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
X_train, X_test = X_train / 255.0, X_test / 255.0

# Reshape the input data for CNN
X_train = X_train.reshape((60000, 28, 28, 1))
X_test = X_test.reshape((10000, 28, 28, 1))

# LeNet-5 model
model = models.Sequential()
model.add(layers.Conv2D(6, (3, 3), activation='tanh', input_shape=(28, 28, 1)))  # Adjusted filter size
model.add(layers.AveragePooling2D(2))
model.add(layers.Activation('sigmoid'))
model.add(layers.Conv2D(16, (3, 3), activation='tanh'))  # Adjusted filter size
model.add(layers.AveragePooling2D(2))
model.add(layers.Activation('sigmoid'))
model.add(layers.Conv2D(120, (3, 3), activation='tanh'))  # Adjusted filter size
model.add(layers.Flatten())
model.add(layers.Dense(84, activation='tanh'))
model.add(layers.Dense(10, activation='softmax'))

# List of optimizers to compare
optimizers = ['SGD', 'SGDM', 'Adagrad', 'RMSProp', 'Adam']

# Initialize lists to store results
history_dict = {}
test_accuracies = []
test_losses = []

# Train the model with each optimizer and store results
for optimizer_name in optimizers:
    # Clear previous session to avoid conflicts
    tf.keras.backend.clear_session()

    # Create optimizer based on the optimizer_name
    if optimizer_name == 'SGD':
        optimizer = tf.keras.optimizers.SGD()
    elif optimizer_name == 'SGDM':
        optimizer = tf.keras.optimizers.SGD(momentum=0.9)
    elif optimizer_name == 'Adagrad':
        optimizer = tf.keras.optimizers.Adagrad()
    elif optimizer_name == 'RMSProp':
        optimizer = tf.keras.optimizers.RMSprop()
    elif optimizer_name == 'Adam':
        optimizer = tf.keras.optimizers.Adam()

    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    start_time = time.time()
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), verbose=1)
    print(f'Optimizer: {optimizer_name}, Fit Time: {time.time() - start_time}')

    # Evaluate the model on the test data
    score = model.evaluate(X_test, y_test)
    test_losses.append(score[0])
    test_accuracies.append(score[1])

    # Store training history for later plotting
    history_dict[optimizer_name] = history.history

# Plot the training history for each optimizer
plt.figure(figsize=(12, 8))

for optimizer_name, history in history_dict.items():
    plt.plot(history['accuracy'], label=f'{optimizer_name}')

plt.title('LeNet on MNIST')
plt.xlabel('Epoch')
plt.ylabel('Validation Accuracy')
plt.legend()
plt.show()

plt.figure(figsize=(12, 8))

for optimizer_name, history in history_dict.items():
    plt.plot(history['loss'], label=f'{optimizer_name}')

plt.title('LeNet on MNIST')
plt.xlabel('Epoch')
plt.ylabel('Validation Loss')
plt.legend()
plt.show()

# Display test accuracies and losses
for optimizer_name, test_accuracy, test_loss in zip(optimizers, test_accuracies, test_losses):
    print(f'Test Accuracy ({optimizer_name}): {test_accuracy:.4f}, Test Loss ({optimizer_name}): {test_loss:.4f}')
