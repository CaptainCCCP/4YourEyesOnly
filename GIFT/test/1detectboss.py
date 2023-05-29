import cv2
import numpy as np
import pyautogui
import time

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(r'Q:\Anaconda\Lib\haarcascades\haarcascade_frontalface_default.xml')

# Load the image of your boss's face
boss_face = cv2.imread('boss_img.jpg', cv2.IMREAD_GRAYSCALE)

# Define the threshold for face detection confidence
face_confidence = 0.5

# Define the threshold for face identification confidence
boss_confidence = 0.7

# Define the coordinates of the working page on explorer
working_page_x = 100
working_page_y = 100

# Start capturing the screen
while True:
    # Capture the screen
    img = pyautogui.screenshot()

    # Convert the image to grayscale
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Iterate through the detected faces
    for (x, y, w, h) in faces:
        # Extract the face from the image
        face = gray[y:y+h, x:x+w]

        # Resize the face to match the size of the boss's face
        face = cv2.resize(face, (boss_face.shape[1], boss_face.shape[0]))

        # Compare the face to the boss's face using the normalized cross correlation (NCC) method
        ncc = cv2.matchTemplate(face, boss_face, cv2.TM_CCORR_NORMED)[0][0]

        # If the NCC score is above the threshold, it's your boss's face
        if ncc > boss_confidence:
            # Shift the screen to the working page on explorer
            pyautogui.moveTo(working_page_x, working_page_y)
            pyautogui.click()
            break
    else:
        # If no faces were detected, wait for a while to avoid excessive CPU usage
        time.sleep(0.1)