#2022-12-01

import requests
import numpy as np
from matplotlib import pyplot as plt

req = requests.get("http://192.168.6.172:8000/readings.json")
data = req.json()
readings = data["readings"][0]
print(len(readings))

temp = []
for sample in readings:
    if sample["sensor_id"] == 1:
        temp.append(sample["value"])
print(len(temp))

#Every 12 samples calculate the mean and std
number_samples_per_hour = 12
mean_per_hour = []
std_per_hour = []
top_per_hour = []
bottom_per_hour = []
x = []
for i in range(0, len(temp), number_samples_per_hour):
    mean_per_hour.append(np.mean(temp[i:i+number_samples_per_hour]))
    std_per_hour.append(np.std(temp[i:i+number_samples_per_hour]))
    top_per_hour.append(mean_per_hour[-1] + std_per_hour[-1])
    bottom_per_hour.append(mean_per_hour[-1] - std_per_hour[-1])
    x.append(i)

fig=plt.figure(figsize=(9,9))
plt.subplot(3,1,1)
plt.plot(temp)
plt.subplot(3,1,2)
plt.plot(x,mean_per_hour)
plt.subplot(3,1,3)
plt.plot(x,mean_per_hour)
plt.fill_between(x, top_per_hour, bottom_per_hour, alpha=0.5,color="#8ecae6", linewidth=5)
plt.show()
