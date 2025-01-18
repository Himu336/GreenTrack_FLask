# Greenery Percentage Prediction - Green Pioneers Hackathon

This project is a web-based application that predicts the percentage of greenery (trees and vegetation) in an uploaded image. It uses deep learning for vegetation analysis and Flask for web application development. The goal is to facilitate the analysis of greenery in any given image, helping to track and promote environmental sustainability.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Model Information](#model-information)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project uses a U-Net model to predict the percentage of greenery in an image. The user uploads an image through a web interface, and the backend calculates and displays the percentage of the image covered by trees or vegetation.

### Technologies Used
- **Flask**: Web framework for handling HTTP requests and serving web pages.
- **TensorFlow/Keras**: Deep learning framework to load and use a pre-trained model for greenery detection.
- **OpenCV**: Used for image processing tasks, such as reading and resizing images.
- **Leaflet**: For displaying a map interface in the frontend.
- **HTML/CSS/JavaScript**: Frontend technologies for UI and interaction.

## Features

- **Image Upload**: Users can upload an image for analysis.
- **Greenery Percentage Calculation**: The application uses a pre-trained U-Net model to calculate the percentage of greenery (trees and vegetation) in the uploaded image.
- **Map Integration**: Users can interact with a map, and even capture a map image to analyze its greenery content.
- **Real-Time Analysis**: Instant prediction results are shown after the user uploads an image.

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/greenery-percentage-prediction.git
cd greenery-percentage-prediction
```

### 2. Install Dependencies

Create a virtual environment and install the required dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Download the Pre-trained Model

The pre-trained model is used for predicting the greenery percentage. You need to download the `unet_forest_model.h5` model and place it in the `models` directory.

- [Download the model here](link_to_model) and place it in the `models/` directory.

### 4. Run the Application

Start the Flask server:

```bash
python application.py
```

Visit `http://127.0.0.1:5000` in your browser to interact with the application.

## Usage

1. Upload an image by clicking the “Choose File” button.
2. Once the image is uploaded, the system will process it and display the greenery percentage.
3. Use the map interface to capture map images and analyze the greenery percentage.

### Upload Form

The image upload form allows the user to select and upload images of vegetation. Upon submitting the form, the backend processes the image and returns the greenery percentage.

### Greenery Percentage Prediction

The model predicts the percentage of greenery in the uploaded image using the U-Net architecture. The result is displayed on the webpage once the prediction is complete.

## File Structure

Here is the file structure of the project:

```
greenery-percentage-prediction/
├── application.py              # Main Flask application file
├── index.html                  # Frontend HTML file with image upload and map interface
├── requirements.txt            # List of dependencies
├── models/
│   └── unet_forest_model.h5    # Pre-trained model for greenery prediction
├── static/
│   └── css/
│       └── style.css           # Custom CSS for styling the frontend
└── uploads/                    # Directory for storing uploaded images
```

## Model Information

The model used in this application is based on the **U-Net** architecture, specifically trained for vegetation (forest) segmentation. The model takes an image as input and outputs a binary mask indicating areas covered by greenery. The percentage of greenery is then calculated based on the size of the green regions relative to the total image size.

## Contributing

Feel free to contribute to this project by forking the repository, making changes, and submitting pull requests.

### How to Contribute
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
