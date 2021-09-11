import serial
import time

import numpy as np

def arduino_run():
    arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
    while True:
        for i in range(255):
            # arduino.write(str(i).encode('ascii'))
            byte_string = bytes(str(i), encoding='utf-8')
            arduino.write(byte_string)
            print(byte_string)
            time.sleep(0.01)

if __name__ == "__main__":
    arduino_run()