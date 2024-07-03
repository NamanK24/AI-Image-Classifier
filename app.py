import tkinter as tk
from tkinter import simpledialog, messagebox
import cv2 as cv
import os
import PIL.Image, PIL.ImageTk
import model
import camera


class App:

    def __init__(self, window=None, window_title="Camera Classifier"):
        if window is None:
            window = tk.Tk()
        self.window = window
        self.window.title(window_title)

        self.counters = [1, 1]
        self.model = model.Model()
        self.auto_predict = False

        try:
            self.camera = camera.Camera()
        except ValueError as e:
            messagebox.showerror("Camera Error", str(e))
            self.window.quit()
            return

        self.init_gui()

        self.delay = 15
        self.update()

        self.window.attributes("-topmost", True)
        self.window.mainloop()

    def init_gui(self):
        self.canvas = tk.Canvas(
            self.window, width=self.camera.width, height=self.camera.height
        )
        self.canvas.pack()

        self.btn_toggleauto = tk.Button(
            self.window,
            text="Auto Prediction",
            width=50,
            command=self.auto_predict_toggle,
        )
        self.btn_toggleauto.pack(anchor=tk.CENTER, expand=True)

        self.classname_one = simpledialog.askstring(
            "Classname One", "Enter the name of the first class:", parent=self.window
        )
        self.classname_two = simpledialog.askstring(
            "Classname Two", "Enter the name of the second class:", parent=self.window
        )

        self.btn_class_one = tk.Button(
            self.window,
            text=self.classname_one,
            width=50,
            command=lambda: self.save_for_class(1),
        )
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(
            self.window,
            text=self.classname_two,
            width=50,
            command=lambda: self.save_for_class(2),
        )
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(
            self.window, text="Train Model", width=50, command=self.train_model
        )
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_predict = tk.Button(
            self.window, text="Predict", width=50, command=self.predict
        )
        self.btn_predict.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = tk.Button(
            self.window, text="Reset", width=50, command=self.reset
        )
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.class_label = tk.Label(self.window, text="CLASS")
        self.class_label.config(font=("Arial", 20))
        self.class_label.pack(anchor=tk.CENTER, expand=True)

    def auto_predict_toggle(self):
        self.auto_predict = not self.auto_predict

    def save_for_class(self, class_num):
        ret, frame = self.camera.get_frame()
        if not ret:
            messagebox.showerror("Camera Error", "Failed to capture frame")
            return

        os.makedirs(str(class_num), exist_ok=True)

        filename = f"{class_num}/frame{self.counters[class_num-1]}.jpg"
        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        resized = cv.resize(gray, (150, 150))  # Resize to 150x150
        cv.imwrite(filename, resized)

        self.counters[class_num - 1] += 1

    def train_model(self):
        try:
            self.model.train_model(self.counters)
            messagebox.showinfo(
                "Training Complete", "Model has been successfully trained!"
            )
        except Exception as e:
            messagebox.showerror("Training Error", f"Failed to train model: {str(e)}")

    def reset(self):
        for folder in ["1", "2"]:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    messagebox.showerror(
                        "Reset Error", f"Failed to delete {file_path}: {str(e)}"
                    )

        self.counters = [1, 1]
        self.model = model.Model()
        self.class_label.config(text="CLASS")

    def update(self):
        if self.auto_predict:
            self.predict()

        ret, frame = self.camera.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)

    def predict(self):
        frame = self.camera.get_frame()
        if frame[0]:
            try:
                prediction = self.model.predict(frame)
                if prediction == 1:
                    self.class_label.config(text=self.classname_one)
                elif prediction == 2:
                    self.class_label.config(text=self.classname_two)
                else:
                    self.class_label.config(text="Unknown")
            except Exception as e:
                messagebox.showerror("Prediction Error", f"Failed to predict: {str(e)}")
        else:
            messagebox.showerror(
                "Camera Error", "Failed to capture frame for prediction"
            )


if __name__ == "__main__":
    App(window_title="Camera Classifier v0.1 Alpha")
