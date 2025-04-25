import time
import matplotlib
import serial
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.use("TkAgg")

arduino = serial.Serial('/dev/cu.usbserial-110', baudrate=9600, timeout=.1)


def get_data():
    data =""
    while len(data) < 1:
        data = arduino.readline()
    return data


rpms = []

for i in range(55):
    time.sleep(0.1)
    data = get_data()
    msg = data.decode('utf-8')
    rpm, act, error = msg.strip().split(',')
    print(f"Error: {error}, Actual: {act}, RPM: {rpm}")
    rpms.append(float(float(rpm)))

plt.plot(rpms)
plt.hlines(y=sum(rpms)/len(rpms),xmin=0,xmax=len(rpms),color='r')
plt.show()
print(sum(rpms)/len(rpms))