# Hand Gesture Keyboard

**Note: This code will only run in Python versions below 3.10 due to compatibility issues with the mediapipe library.**

## Purpose

Implementation of Hand Gesture Keyboard that detects hand gestures using OpenCV and the HandTrackingModule. It tracks hand movements from a webcam and associates them with keyboard buttons. Users can interact by hovering over buttons and performing a click gesture by bringing the tip of their index finger close to the middle finger. The code utilizes OpenCV, HandTrackingModule, time, numpy, and pynput.keyboard libraries. It offers a creative and engaging method for text input, transforming user experiences through intuitive hand movements.

## Installation

- Install the required libraries by running `pip install mediapipe opencv-python numpy pynput`.

## Usage

1. Run the project using `python HandGestureKeyboard.py`.
2. A window will open showing the camera feed.
3. Place your hand in front of the camera.
4. Match your hand gestures to the buttons displayed on the screen.
5. When a button is highlighted, bring your index finger close to your thumb to press it.
6. The pressed key will be displayed in the rectangle at the bottom of the screen.
7. To exit the program, press the 'q' key.

## Code Structure

- `HandTrackingModule.py`: Module that provides hand tracking functionality.
- `drawAll()`: Function to draw the buttons on the screen.
- `Button` class: Represents a button with its position, size, and corresponding text.
- Main loop:
  - Captures frames from the camera.
  - Detects hand landmarks and bounding box information.
  - Draws the buttons on the screen.
  - Checks if any button is within the range of the hand landmarks.
  - Detects a button press based on the distance between landmarks.
  - Displays the pressed key and updates the final text.
  - Shows the modified image in a window.

## Known Issues

- The code assumes a single hand in the frame and may not work correctly with multiple hands.

## License

This project is licensed under the [MIT License](LICENSE).

For more information, please refer to the [license file](LICENSE).

For questions or support, please contact [Ankit Pakhale](mailto:akp3067@gmail.com).
