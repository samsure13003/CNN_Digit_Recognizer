# 🔢 CNN Digit Recognizer

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Keras](https://img.shields.io/badge/Keras-CNN-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
[![MNIST](https://img.shields.io/badge/Dataset-MNIST-blue?style=for-the-badge)](http://yann.lecun.com/exdb/mnist/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A real-time handwritten digit recognition web app powered by a **Convolutional Neural Network (CNN)** trained on the MNIST dataset. Draw any digit (0–9) on the canvas and get an instant prediction with confidence score — all running through a Flask API backend.

---

## 🎯 Demo

> Draw a digit on the canvas → Click **Predict** → Get the result instantly!

![Demo Preview](demo.gif)

---

## 🧠 Model Architecture

The CNN is built with TensorFlow/Keras and trained on the classic **MNIST dataset** (60,000 training images, 10,000 test images).

```
Input (28×28×1)
     │
     ▼
Conv2D (32 filters, 3×3, ReLU)
     │
MaxPooling2D (2×2)
     │
Conv2D (64 filters, 3×3, ReLU)
     │
MaxPooling2D (2×2)
     │
Flatten
     │
Dense (64, ReLU)
     │
Dense (10, Softmax)  ← Output: Digit 0–9
```

| Layer | Output Shape | Parameters |
|---|---|---|
| Conv2D (32 filters) | 26×26×32 | 320 |
| MaxPooling2D | 13×13×32 | 0 |
| Conv2D (64 filters) | 11×11×64 | 18,496 |
| MaxPooling2D | 5×5×64 | 0 |
| Flatten | 1600 | 0 |
| Dense (64) | 64 | 102,464 |
| Dense (10) | 10 | 650 |

- **Optimizer:** Adam  
- **Loss:** Sparse Categorical Crossentropy  
- **Training Epochs:** 5  

---

## 🗂️ Project Structure

```
cnn-digit-recognizer/
│
├── model.py          # CNN architecture definition
├── train.py          # Model training script (MNIST)
├── app.py            # Flask API backend
├── index.html        # Frontend canvas UI
├── cnn_model.h5      # Saved trained model
└── README.md
```

---

## ⚙️ How It Works

```
User draws on canvas
        │
        ▼
Canvas → Base64 PNG (JavaScript)
        │
        ▼
POST /predict  (Flask API)
        │
        ▼
Decode → Grayscale → Resize 28×28 → Normalize
        │
        ▼
CNN Model Inference
        │
        ▼
{ digit: 7, confidence: 0.9983 }
        │
        ▼
Display result on UI
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install tensorflow flask flask-cors pillow numpy
```

### 1. Train the Model

```bash
python train.py
```

This downloads the MNIST dataset, trains the CNN for 5 epochs, and saves `cnn_model.h5`.

### 2. Start the Flask API

```bash
python app.py
```

The API will run at `http://127.0.0.1:5000`

### 3. Open the Frontend

Open `index.html` directly in your browser — no server needed for the frontend.

---

## 🌐 API Reference

### `POST /predict`

Accepts a base64-encoded image and returns the predicted digit.

**Request Body:**
```json
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANS..."
}
```

**Response:**
```json
{
  "digit": 7,
  "confidence": 0.9983
}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Deep Learning | TensorFlow 2.x / Keras |
| Backend API | Flask + Flask-CORS |
| Image Processing | Pillow (PIL) |
| Frontend | HTML5 Canvas + Vanilla JS |
| Dataset | MNIST (via `tf.keras.datasets`) |

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Training Accuracy | ~99% |
| Test Accuracy | ~99% |
| Training Epochs | 5 |
| Input Size | 28×28 grayscale |

---

## 🔮 Future Improvements

- [ ] Deploy to cloud (Heroku / Render / HuggingFace Spaces)
- [ ] Add digit history log on the UI
- [ ] Display confidence bar chart for all 10 classes
- [ ] Support for touch drawing on mobile
- [ ] Convert to a Streamlit or React app

---

## 👨‍💻 Author

**Samsur**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/your-username)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> *"From pixels to predictions — one convolution at a time."*
