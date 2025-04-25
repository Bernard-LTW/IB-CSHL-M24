#2022-12-05 Quiz 032
#Prompt : Compare the data from sensor #9 and sensor #10 with smoothing of 12 samples

import requests
import numpy as np
from matplotlib import pyplot as plt

req = requests.get("http://192.168.6.142/readings")
data = req.json()
readings = data["readings"][0]

temp1 = []
temp2 = []
samples1 = []
samples2 = []
for i in range(len(readings)):
    if readings[i]["sensor_id"] == 9:
        temp1.append(readings[i]["value"])
        samples1.append(i)
    if readings[i]["sensor_id"] == 10:
        temp2.append(readings[i]["value"])
        samples2.append(i)

print(temp1)
print(temp2)

number_samples_per_hour = 12
mean_per_hour = []
std_per_hour = []
top_per_hour = []
bottom_per_hour = []
x = []
mean_per_hour2 = []
std_per_hour2 = []
top_per_hour2 = []
bottom_per_hour2 = []
x2 = []

for i in range(0, len(temp1), number_samples_per_hour):
    mean_per_hour.append(np.mean(temp1[i:i+number_samples_per_hour]))
    std_per_hour.append(np.std(temp1[i:i+number_samples_per_hour]))
    top_per_hour.append(mean_per_hour[-1] + std_per_hour[-1])
    bottom_per_hour.append(mean_per_hour[-1] - std_per_hour[-1])
    x.append(i)

for i in range(0, len(temp2), number_samples_per_hour):
    mean_per_hour2.append(np.mean(temp2[i:i+number_samples_per_hour]))
    std_per_hour2.append(np.std(temp2[i:i+number_samples_per_hour]))
    top_per_hour2.append(mean_per_hour2[-1] + std_per_hour2[-1])
    bottom_per_hour2.append(mean_per_hour2[-1] - std_per_hour2[-1])
    x2.append(i)

difference = []
if len(mean_per_hour) == len(mean_per_hour2):
    for i in range(len(mean_per_hour)):
        difference.append(mean_per_hour[i] - mean_per_hour2[i])



fig = plt.figure(figsize=(9,12))
plt.subplot(3,1,1)
plt.plot(x,mean_per_hour)
plt.title("Sensor 9")
plt.subplot(3,1,2)
plt.plot(x2,mean_per_hour2, color="green")
plt.title("Sensor 10")
plt.subplot(3,1,3)
#fill between the differences of the means of the two sensors
plt.plot(x,difference, color="red")
plt.title("Difference")
plt.show()
