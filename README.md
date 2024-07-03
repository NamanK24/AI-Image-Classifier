# AI Image Classifier

AI Image Classifier is an interactive, real-time tool that transforms your webcam into a smart object recognizer.
With its user-friendly interface, you can quickly train a custom AI model on two categories of your choice. 
Capture a few images, train the model with a single click, and watch as it instantly classifies new objects shown to your camera. 
Whether you're an educator demonstrating AI concepts, a developer prototyping ideas, or an enthusiast exploring machine learning, AI Image Classifier makes artificial intelligence accessible and engaging.
From distinguishing fruits to identifying household items, this application brings the power of AI-driven image classification to your fingertips in minutes, 
making it both educational and fun to use.


## Features

Certainly! Here's a list of the key features of the AI Image Classifier project:

1. Real-time Webcam Integration:
   - Live video feed display
   - Instant image capture for training and classification

2. Custom Classification Categories:
   - User-defined class names
   - Support for two distinct categories

3. Simple Training Process:
   - One-click image capture for each category
   - Easy-to-use "Train Model" button

4. Machine Learning Model:
   - Utilizes scikit-learn's LinearSVC for classification
   - Quick training on captured images

5. Real-time Prediction:
   - Instant classification of live webcam feed
   - Clear display of predicted category

6. Auto-Prediction Mode:
   - Toggle for continuous, hands-free classification
   - Real-time updates of predictions

7. User-Friendly GUI:
   - Intuitive button layout
   - Large, clear display of current classification

8. Reset Functionality:
   - Option to clear all training data
   - Ability to start fresh with new categories

9. Error Handling:
   - Informative error messages
   - Graceful handling of common issues (e.g., camera not found)

10. Cross-platform Compatibility:
    - Works on Windows, macOS, and Linux (with Python and required libraries installed)

11. Customizable Image Processing:
    - Images are automatically resized and converted to grayscale for consistency


## Technologies Used

Certainly! Here's a list of the key technologies used in the AI Image Classifier project:

1. Programming Language:
   - Python 3.8.10

2. Graphical User Interface (GUI):
   - Tkinter: Python's standard GUI package

3. Computer Vision and Image Processing:
   - OpenCV (cv2): For capturing and processing webcam images

4. Machine Learning:
   - scikit-learn: Specifically, the LinearSVC (Linear Support Vector Classification) model for image classification

5. Image Handling:
   - PIL (Python Imaging Library): For advanced image processing tasks

6. Numerical Computing:
   - NumPy: For efficient array operations and numerical computations

7. File System Operations:
   - os module: For directory and file management

8. Error Handling and User Interaction:
   - Built-in Python exceptions and Tkinter's messagebox for displaying alerts and errors



## Installation and Usage
Make sure to use Python 3.8.10

Install all the required libraries
```bash
pip install -r requirements.txt
```

To run, go to the main.py folder and use the following command (in the terminal):
```bash
python main.py
```
