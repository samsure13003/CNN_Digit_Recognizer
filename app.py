from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import tensorflow as tf
import base64
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = tf.keras.models.load_model("cnn_model.h5")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["image"]

    # Decode base64 image
    image = base64.b64decode(data.split(",")[1])
    image = Image.open(io.BytesIO(image)).convert("L")
    image = image.resize((28,28))

    img = np.array(image) / 255.0
    img = img.reshape(1,28,28,1)

    prediction = model.predict(img)
    digit = int(np.argmax(prediction))

    return jsonify({
        "digit": digit,
        "confidence": float(np.max(prediction))
    })

if __name__ == "__main__":
    app.run(debug=True)