import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Load the pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Access the webcam (you can specify a different index if you have multiple cameras)
cap = cv2.VideoCapture(0)

def capture_image():
    ret, frame = cap.read()
    cv2.imwrite('captured_image.jpg', frame)  # Save the frame as an image
    print("Image captured!")

def show_frame():
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    img = ImageTk.PhotoImage(image=img)
    panel.img = img
    panel.config(image=img)
    panel.after(10, show_frame)

root = tk.Tk()
root.title("Capture Image")

panel = tk.Label(root)
panel.pack(padx=10, pady=10)

capture_button = tk.Button(root, text="Capture Image", command=capture_image)
capture_button.pack(padx=10, pady=5)

show_frame()  # Start displaying the webcam feed

root.mainloop()

# Release the webcam
cap.release()
