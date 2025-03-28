from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import os

# Load the trained model
model = keras.models.load_model("digit_model.h5")

# Create a Flask app
app = Flask(__name__)

# Ensure the "static/uploads" directory exists
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Function to preprocess the uploaded image
def preprocess_image(image_path):
    img = Image.open(image_path).convert("L")  # Convert to grayscale
    img = img.resize((28, 28))  # Resize to 28x28
    img = np.array(img) / 255.0  # Normalize pixel values to [0,1]
    img = img.reshape(1, 28, 28)  # Reshape for model input
    return img

@app.route("/", methods=["GET", "POST"])
def upload_and_predict():
    if request.method == "POST":
        # Get the uploaded file
        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        # Save the uploaded file
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Preprocess the image
        processed_img = preprocess_image(file_path)

        # Make prediction
        prediction = model.predict(processed_img)
        predicted_digit = np.argmax(prediction)  # Get the highest probability class

        return render_template("index.html", filename=file.filename, digit=predicted_digit)

    return render_template("index.html", filename=None, digit=None)

if __name__ == "__main__":
    app.run(debug=True)
