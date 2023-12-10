# Import the library to interface with GPIO pins
# This requires the RPi.GPIO package to be installed: "pip install RPi.GPIO"
import RPi.GPIO as GPIO

# Import the time library to use the delay function
import time

# Sets the numbering scheme for the pins, either BCM (the "GPIOxx" number from Broadcom) or BOARD (the pin number on the header 1-40)
GPIO.setmode(GPIO.BCM)

# Pick the GPIO pin we want (21 for GPIO.BCM, 40 for GPIO.BOARD)
output_channel = 21

# Sets the operating mode for the selected pin (either OUT or IN)
GPIO.setup(output_channel, GPIO.OUT)

output_on = False

# Start an infinite loop
while True:
    # Wait a second
    time.sleep(1)

    # Toggle the output
    if not output_on:
        # Turn on the output
        GPIO.output(output_channel, GPIO.HIGH)
        output_on = True
    else:
        # Turn off the output
        GPIO.output(output_channel, GPIO.LOW)
        output_on = False