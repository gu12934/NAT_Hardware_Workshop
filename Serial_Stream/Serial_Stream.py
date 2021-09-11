import serial
import time

import numpy as np

def arduino_run():
    arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
    while True:
        b = arduino.readline()
        # print(b)

        newstring = b.decode()
        # print(newstring)

        string = newstring.rstrip()
        print(string)

if __name__ == "__main__":
    arduino_run()

 