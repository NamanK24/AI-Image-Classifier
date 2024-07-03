from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL.Image
import os


class Model:

    def __init__(self):
        self.model = LinearSVC()
        self.image_size = (150, 150)  # Define a standard image size

    def train_model(self, counters):
        img_list = []
        class_list = []

        for class_num, counter in enumerate(counters, start=1):
            for i in range(1, counter):
                try:
                    img = cv.imread(f"{class_num}/frame{i}.jpg", cv.IMREAD_GRAYSCALE)
                    if img is None:
                        raise IOError(f"Failed to read image: {class_num}/frame{i}.jpg")
                    img = cv.resize(img, self.image_size)  # Resize to standard size
                    img = img.flatten()  # Flatten the image
                    img_list.append(img)
                    class_list.append(class_num)
                except Exception as e:
                    print(f"Error processing image {class_num}/frame{i}.jpg: {str(e)}")

        if not img_list:
            raise ValueError("No valid images found for training")

        img_list = np.array(img_list)
        class_list = np.array(class_list)

        self.model.fit(img_list, class_list)
        print("Model successfully trained!")

    def predict(self, frame):
        ret, frame = frame
        if not ret:
            raise ValueError("Invalid frame for prediction")

        try:
            # Convert to grayscale and resize
            gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
            resized = cv.resize(gray, self.image_size)

            # Flatten the image
            flattened = resized.flatten()

            # Predict
            prediction = self.model.predict([flattened])

            return prediction[0]
        except Exception as e:
            raise ValueError(f"Prediction failed: {str(e)}")
