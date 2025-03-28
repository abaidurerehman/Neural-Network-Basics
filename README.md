# Neural Network Basics

## 📌 Project Overview
This project demonstrates the fundamentals of neural networks using the **MNIST dataset**. It includes:
- Data preprocessing and augmentation
- Building a **Convolutional Neural Network (CNN)** using TensorFlow/Keras
- Training and evaluating the model
- Deploying the model with a Flask web app for digit recognition

## 📂 Project Structure
```
Neural-Network-Basics/
│── train_model.py          # Train the CNN model and save it
│── app.py                  # Flask app for digit recognition
│── static/
│   ├── digit_0.png         # Sample images for testing
│   ├── digit_1.png         # ...
│── templates/
│   ├── index.html          # Web UI for uploading images
│── digit_model.h5          # Saved trained model
│── requirements.txt        # Required dependencies
│── README.md               # Project documentation
```

## 🚀 Installation & Setup
### 1️⃣ Create and Activate Virtual Environment
```bash
# For Conda
conda create -n tf_env python=3.8
conda activate tf_env

# Or for virtualenv
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model
```bash
python train_model.py
```
This will:
- Load the **MNIST dataset**
- Normalize and preprocess images
- Train a CNN model
- Save the trained model as `digit_model.h5`

### 4️⃣ Run the Flask App
```bash
python app.py
```
Access the web app at: **`http://127.0.0.1:5000`**

## 🎯 Features
✔️ Loads and preprocesses MNIST dataset  
✔️ CNN model with **Conv2D, MaxPooling2D, and Dense layers**  
✔️ Model training with data augmentation  
✔️ Saves trained model (`.h5` format)  
✔️ Flask web app for real-time digit recognition  
✔️ Interactive UI for uploading and predicting digits  

## 📊 Model Performance
The trained model achieves **high accuracy** on the MNIST dataset. Sample output:
```bash
Test Accuracy: 98.5%
```

## 🔧 Troubleshooting
- If **Matplotlib is missing**, install it:
  ```bash
  pip install matplotlib
  ```
- If **Flask app gives a 404 error**, ensure `index.html` is in the `templates/` folder.

## 📜 License
This project is open-source under the **MIT License**.

---

