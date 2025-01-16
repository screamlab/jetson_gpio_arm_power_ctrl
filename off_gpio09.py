import Jetson.GPIO as GPIO
import time

# Set up the GPIO mode to BOARD (using physical pin numbering)
GPIO.setmode(GPIO.BOARD)

# Define the pin number
pin = 7

# Set up GPIO9 as an output
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()
