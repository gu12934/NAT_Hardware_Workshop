import serial
import random
import time

import numpy as np

wait = 0.1
past_time = time.time()

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
if arduino.in_waiting:
    junk = arduino.readline().strip() # clean any junk from the buffer
    print("junk: " + junk[-10:].decode("utf-8")) 
  
def arduino_run():
    cur_time = time.time()
    global past_time

    if cur_time - past_time >= 0.02:
        past_time = cur_time
        # Grab sensor data
        b = arduino.readline()
        newstring = b.decode()
        string = newstring.rstrip()
        print(string)

        # Send back a place holder value for light
        byte_string = (str(random.randrange(0, 255)) + 'n').encode('ascii')
        arduino.write(byte_string)
        print(byte_string)
        time.sleep(wait)

if __name__ == "__main__":
    while True:
        arduino_run()