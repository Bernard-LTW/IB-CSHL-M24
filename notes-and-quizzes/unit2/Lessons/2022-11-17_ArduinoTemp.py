import serial
import time
import matplotlib.pyplot as plt

arduino = serial.Serial('/dev/cu.usbserial-10', baudrate=9600, timeout=.1)
temp_list = []
humidity_list = []

plt.style.use = "ggplot"

def getTemp():
    data = ""
    while len(data)<1:
        data = arduino.readline()
    return data

for i in range(50):
    time.sleep(0.1)
    value = getTemp()
    msg = value.decode("utf-8")
    print(msg)
    if msg != "Hello\r\n":
        slicedata = msg.split(" ")
        print(slicedata)
        humidity = (slicedata[0].split(":")[1])
        humidity = float(humidity.replace("%",""))
        print(humidity)
        temp = (slicedata[1].split(":")[1])
        temp = float(temp.replace("C",""))
        print(temp)

        temp_list.append(temp)
        humidity_list.append(humidity)

print(temp_list)
print(humidity_list)

fig = plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(temp_list, color="red")
plt.title("Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.subplot(1,2,2)
plt.plot(humidity_list, color="blue")
plt.title("Humidity")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")

plt.show()


