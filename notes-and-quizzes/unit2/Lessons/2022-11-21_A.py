#2022-11-21 A

import requests
from matplotlib import pyplot as plt

req = requests.get("http://192.168.6.142/readings")
data = req.json()
readings = data["readings"][0]
print(len(readings))

temp = []
for sample in readings:
    if sample["sensor_id"] == 2:
        temp.append(sample["value"])

plt.plot(temp)
plt.show()