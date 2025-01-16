# Jetson GPIO Arm Power Control

This repository controls GPIO09 on the Jetson Orin Nano Developer Kit.

GPIO09 is connected to the Normally Closed (NC) pin of the relay, which manages the power supply to the robot arm. When GPIO09 is set to high, the relay opens, cutting off the power to the robot arm. Conversely, when GPIO09 is set to low, the relay closes, restoring power to the robot arm.



## Usage

- To power off the robot arm, execute the following command:

  ```bash
  python on_gpio09.py
  ```

- To power on the robot arm, execute the following command:

  ```bash
  python off_gpio09.py
  ```