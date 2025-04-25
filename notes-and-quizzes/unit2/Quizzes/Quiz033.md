# Quiz 033

## Part A Prompt

Compare the data from sensor #6,8,9,10 by calculating and plotting the mean value of 500 samples.

## Code Structure

### Main Program
```.py
#2022-12-09 Quiz 033

#Compare the data from sensor #6,8,9,10 by calculating and plotting the mean value of 500 samples.

from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec

import unit2_lib as u2l

sensors = [6,8,9,10]
values = []
for s in sensors:
    x,smoothed = u2l.smoothing(u2l.get_readings(s)[:500])
    values.append(smoothed)

mean_per_hour = []
for i in range(len(values[0])):
    data = [values[n][i] for n in range(4)]
    mean_per_hour.append(sum(data)/len(sensors))
print("Ready to plot")

fig=plt.figure(figsize=(12,12))
gs = GridSpec(4, 4, figure=fig)
ax = fig.add_subplot(gs[:,0:3])
plt.title("Average of sensors")
plt.plot(x, mean_per_hour)
plt.ylim([20,28])
plt.xlabel("Samples per hour")
plt.ylabel("Celsius")

for row, my_color in [(0,"#e63946"),(1,"#a8dadc"),(2,"#457b9d"),(3,"#1d3557")]:
    ax = fig.add_subplot(gs[row,3])
    plt.plot(x, values[row], color=my_color)
    plt.title("Sensor "+str(sensors[row]))

plt.show()
```

### Unit 2 Library
```.py
import requests
#mport numpy as np

def get_readings(id:int, url:str="http://192.168.6.142/readings") -> list:
    req = requests.get(url)
    data = req.json()
    readings = data["readings"][0]
    temp = []
    for sample in readings:
        if sample["sensor_id"] == id:
            temp.append(sample["value"])
    return temp

def smoothing(data:list, size_window:int=12) -> list:
    x = []
    y = []
    for i in range(0, len(data), size_window):
        #print(data[i:i+size_window])
        segment_mean = sum(data[i:i+size_window])/size_window
        y.append(segment_mean)
        x.append(i)
    return x, y
```

## Evidence

![](/Assets/Quiz033_Evidence.jpg)

*Fig.1* **Screenshot showing the result of the program**