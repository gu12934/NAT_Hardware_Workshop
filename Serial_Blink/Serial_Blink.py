import serial
import time

import numpy as np

def arduino_run():
    arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
    while True:
        time.sleep(1)
        arduino.write(b'1')
        time.sleep(1)
        arduino.write(b'0')

if __name__ == "__main__":
    arduino_run()