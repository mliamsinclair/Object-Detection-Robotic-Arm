# Object Detection Robotic Arm

This repository contains the code for a robotic arm capable of detecting three primary colored balls. The arm receives serial output from a computer running Python code and Arduino code running on an Arduino Uno.

## Installation

To use this code, you will need the following dependencies:

- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- hidapi (`pip install hidapi`)
- pyserial (`pip install pyserial`)

## Arduino Arm Driver Board Code

The Arduino Arm Driver Board Code is responsible for controlling the robotic arm's movements and actions. It uses the U8glib library for display output and the Servo library for controlling the servos. The code communicates with the Python code via serial communication.

### Dependencies

- U8glib (`#include "U8glib.h"`)
- Servo (`#include <Servo.h>`)
- Wire (`#include <Wire.h>`)
- Adafruit_GFX (`#include <Adafruit_GFX.h>`)

### Variables

- `servopin1`, `servopin2`, `servopin3`, `servopin4`, `servopin5`: Pins used for connecting the servos.
- `pyInput`: Serial input from Python.
- `servo1Angle`, `servo2Angle`, `servo3Angle`, `servo4Angle`, `servo5Angle`: Default servo angles.
- `servo1`, `servo2`, `servo3`, `servo4`, `servo5`: Servo objects for controlling the servos.
- `mode`: Current mode of operation (0 for free motion, 1 for ball by color, 2 for initialization).
- `grabbed`, `bottom2`, `bottom3`, `speed`, `initDone`: Variables used for controlling the arm's movements.
- `redraw`: Flag for indicating if the display needs to be redrawn.
- `grabbedStatement`, `grabDraw`, `offsetStr`: Variables used for displaying information about the grabbed ball.

### Functions

- `setup()`: Initializes the display, servos, and serial communication.
- `loop()`: Main loop that handles the different modes of operation.
- `slowWrite()`: Slows down the rotation speed of the servo and returns the new angle.

## Usage

1. Connect the robotic arm to your computer via USB.
2. Upload the Arduino Arm Driver Board Code to the Arduino Uno.
3. Run the Python code on your computer.
4. Use a gamepad to control the arm's movements and actions.
5. The arm can be operated in two modes:
    - Free Motion: Press the "Select" button on the gamepad to activate. Use the gamepad buttons to control the arm's movements.
    - Ball by Color: Press the "Start" button on the gamepad to activate. Use the gamepad buttons to select and grab balls of different colors.

## Documentation

For more detailed information about this project, please refer to the [documentation](https://mliamsinclair.dev/assets/RoboticArmDocumentation-qFTm2Vyj.pdf).
