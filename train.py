import tensorflow as tf
from model import create_model

# Load dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape
x_train = x_train.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)

# Create model
model = create_model()

# Train
model.fit(x_train, y_train, epochs=5)

# Save
model.save("cnn_model.h5")