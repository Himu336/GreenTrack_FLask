import numpy as np
from tensorflow.keras.models import load_model
import cv2
import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the 'uploads' folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load the model (ensure it's loaded only once when the app starts)
model_path = "C:/External Drive/Devpost/GreenTrack/unet_forest_model.h5"
model = load_model(model_path)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def calculate_forest_percentage(image, model):
    predicted_mask = model.predict(np.expand_dims(image, axis=0))[0]
    binary_mask = (predicted_mask > 0.5).astype(np.uint8)
    forest_percentage = np.sum(binary_mask) / (binary_mask.shape[0] * binary_mask.shape[1]) * 100
    return forest_percentage

@app.route("/", methods=["GET", "POST"])
def index():
    # Serve the index page
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save the uploaded file
        file.save(file_path)

        # Read and process the image
        sample_image = cv2.imread(file_path)
        sample_image = cv2.resize(sample_image, (256, 256)).astype("float32") / 255.0

        # Calculate forest percentage using the model
        forest_percentage = calculate_forest_percentage(sample_image, model)

        # Return the result as JSON
        return jsonify({'prediction_text': f"Greenery percentage: {forest_percentage:.2f}%"})
    
    return jsonify({'error': 'Invalid file format'})

if __name__ == "__main__":
    app.run(debug=True)
