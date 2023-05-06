import cv2
import HandTrackingModule as htm
from time import sleep
import numpy as np
from pynput.keyboard import Controller

# Open the camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the hand detector
detector = htm.HandDetector(detectionCon=0.8)

# Define the layout of the buttons on the keyboard
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        [" "]]

# Variable to store the final text
finalText = ""

# Initialize the keyboard controller
keyboard = Controller()

# Function to draw all the buttons on the screen


def drawAll(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos

        detector.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                            20, rt=0)
        cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
                      (255, 0, 255), cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 40, y + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    # Blend the button image with the original frame (added transparency)
    img = img.copy()
    alpha = 0.6
    mask = imgNew.astype(bool)
    img[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return img

# Class representing a button


class Button():
    def __init__(self, pos, text, size=None):
        if size is None:
            size = [85, 85]

        self.pos = pos
        self.size = size
        self.text = text


# Create the list of buttons based on the keys layout
buttonList = []
for index in range(len(keys)):
    buttonList.extend(Button([100 * x + 50, 100 * index + 50], key)
                      for x, key in enumerate(keys[index]))
while True:
    # Read frames from the camera
    success, img = cap.read()
    img = detector.findHands(img)

    # Get hand landmarks and bounding box info
    lmList, bboxInfo = detector.findPosition(img)

    # Draw all the buttons on the screen
    img = drawAll(img, buttonList)

    if lmList:
        # Iterate through the list of buttons
        for button in buttonList:
            x, y = button.pos  # Get the position of the button
            w, h = button.size  # Get the size of the button

            # Check if the index 8 of lmList (hand landmark) is within the button's boundaries
            if (x < lmList[8][0] < x + w) and (y < lmList[8][1] < y + h):

                # When in range of any button, draw a highlighted rectangle around it
                detector.cornerRect(
                    img, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 10, rt=0, colorC=(0, 0, 255))

                cv2.rectangle(img, button.pos, (x + w, y + h),
                              (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                l, _, _ = detector.findDistance(8, 12, img, draw=False)

                print(f"Hand Positon: {int(l)}")
                # When the button is clicked (distance is less than 30 pixels)
                if int(l) < 30:
                    cv2.rectangle(img, button.pos, (x + w, y + h),
                                  (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                    finalText += button.text
                    keyboard.press(button.text)

                    detector.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                                        20, rt=0, colorC=(255, 255, 255))

                sleep(0.40)

    # Create a rectangle for displaying the final text
    cv2.rectangle(img, (90, 450), (700, 550), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (100, 525),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Image", img)    # Show the modified image
    if cv2.waitKey(1) == ord('q'):  # Wait for the 'q' key to be pressed to exit the program
        break

cap.release()  # Release the video capture
cv2.destroyAllWindows()  # Close all windows

# Project Summery
# Implementation of virtual keyboard that detects hand gestures using OpenCV and the HandTrackingModule. It tracks hand movements from a webcam and associates them with keyboard buttons. Users can interact by hovering over buttons and performing a click gesture by bringing the tip of their index finger close to the middle finger. The code utilizes OpenCV, HandTrackingModule, time, numpy, and pynput.keyboard libraries. It offers a creative and engaging method for text input, transforming user experiences through intuitive hand movements.
