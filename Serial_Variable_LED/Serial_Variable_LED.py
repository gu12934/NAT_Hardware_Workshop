import serial
import time

import numpy as np

explicit = 1
wait = 0.1

def arduino_run():
    arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
    if arduino.in_waiting:
        junk = arduino.readline().strip() # clean any junk from the buffer
        print("junk: " + junk[-10:].decode("utf-8")) 
    while True:
        if explicit == 1:
            time.sleep(2)
            arduino.write(b'0n')
            time.sleep(wait)
            arduino.write(b'1n')
            time.sleep(wait)
            arduino.write(b'2n')
            time.sleep(wait)
            arduino.write(b'3n')
            time.sleep(wait)
            arduino.write(b'4n')
            time.sleep(wait)
            arduino.write(b'5n')
            time.sleep(wait)
            arduino.write(b'6n')
            time.sleep(wait)
            arduino.write(b'7n')
            time.sleep(wait)
            arduino.write(b'8n')
            time.sleep(wait)
            arduino.write(b'9n')
            time.sleep(wait)
            arduino.write(b'10n')
        elif explicit == 0:
            time.sleep(2)
            for i in range(255):
                byte_string = (str(i) + 'n').encode('ascii')
                arduino.write(byte_string)
                print(byte_string)
                time.sleep(wait)

if __name__ == "__main__":
    arduino_run()