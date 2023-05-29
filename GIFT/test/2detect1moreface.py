import cv2
import numpy as np
import pyautogui
import time
# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(r'Q:\Anaconda\Lib\haarcascades\haarcascade_frontalface_default.xml')

# Define the threshold for face detection confidence
face_confidence = 0.5

# Define the coordinates of the working page on explorer
working_page_x = 100
working_page_y = 100

# Initialize the variables for face detection
prev_faces = []
current_faces = []

# Start capturing the screen
while True:
    # Capture the screen
    img = pyautogui.screenshot()

    # Convert the image to grayscale
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Update the current faces
    current_faces = [(x, y, w, h) for (x, y, w, h) in faces if w >= 100 and h >= 100]

    # If there's a new face that's not yours, shift the screen to the working page on explorer
    if len(current_faces) > len(prev_faces) and len(current_faces) > 1:
        new_face = set(current_faces)
        for (x, y, w, h) in new_face.difference(set(prev_faces)):
            pyautogui.moveTo(working_page_x, working_page_y)
            pyautogui.click()
            break

        # Update the previous faces
        prev_faces = current_faces

        # Wait for a while to avoid excessive CPU usage
        time.sleep(0.1)