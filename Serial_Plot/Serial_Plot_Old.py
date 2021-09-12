import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import datetime as dt


# plt.style.use('fivethirtyeight')
# arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
# time.sleep(2)

# voltage = []
# rate = 9600
# time = np.arange(0, 1000, 1000/rate)

# while True:
#     def animate(i):
#         b = arduino.readline()
#         newstring = b.decode()
#         string = newstring.rstrip()

#         voltage.append(float(string))
#         if len(voltage) > 20:
#             voltage.pop(0)

#         plt.plot(voltage)

#     ani = FuncAnimation(plt.gcf(), animate, interval=1000)
#     plt.tight_layout()
#     plt.show()

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)

time.sleep(2)

if arduino.in_waiting:
    junk = arduino.readline().strip() # clean any junk from the buffer
    print("junk: " + junk[-10:].decode("utf-8")) 

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read value
    # cur_val = float(arduino.readline().decode().rstrip())



    # print(cur_val)
    arduino.reset_input_buffer()
    time.sleep(0.001)
    b = arduino.readline()
    # print(b)

    newstring = b.decode()
    # print(newstring)

    string = newstring.rstrip()
    print(string)


    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(float(string))# ys.append(cur_val)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Voltage over Time')
    plt.ylabel('uV')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=25)
plt.show()
