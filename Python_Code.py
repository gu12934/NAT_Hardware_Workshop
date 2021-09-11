import serial
import time

ser = serial.Serial('COM6', 9600)
time.sleep(2)

def ledproject():
    user_input = input("\n Type on / off / quit : ")
    if user_input =="on":
        print("Python says LED is on")
        time.sleep(0.1) 
        ser.write(b'1') 
        ledproject()
    elif user_input =="off":
        print("Python says LED is off...")
        time.sleep(0.1)
        ser.write(b'0')
        ledproject()
    elif user_input =="quit" or user_input == "q":
        print("Program Exiting")
        time.sleep(0.1)
        ser.write(b'0')
        ser.close()
    else:
        print("Invalid input. Type on / off / quit.")
        ledproject()

time.sleep(2)
ledproject()
