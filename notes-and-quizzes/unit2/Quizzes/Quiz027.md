# Quiz 027

## Part A Prompt
Create a program that shows the graph of the data and create a linear (H_model = m*h + b) model for the data.

## Code Structure 
```.py
#2022-11-18 Quiz 027

#Prompt: Create a errorbar graph for the data below.You will need to calculate the mean and standard deviation first

sensorA = [16, 24, 24, 9, 23, 26, 26, 23 ,25, 14]
sensorB = [2, 19, 25, 10, 11, 24, 17, 7, 24, 17]
sensorC = [15, 11, 24, 21, 6, 2, 18, 27, 1, 16]

samples = []
for i in range(len(sensorA)):
    samples.append(i)

import numpy as np
import matplotlib.pyplot as plt

mean_list = []
std_list = []
high_list = []
low_list = []


for i in range(len(sensorA)):
    data = [sensorA[i], sensorB[i], sensorC[i]]
    mean_list.append(np.mean(data))
    std_list.append(np.std(data))
    high_list.append(np.max(data))
    low_list.append(np.min(data))

print(mean_list)
print(std_list)
print(high_list)
print(low_list)
fig = plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.plot(samples, sensorA, color="#2b2d42", label="Sensor A")
plt.plot(samples, sensorB, color="#90e0ef", label="Sensor B")
plt.plot(samples, sensorC, color="#d90429", label="Sensor C")
plt.xlabel("Samples")
plt.ylabel("Values")

plt.subplot(1,2,2)
plt.fill_between(samples, high_list, low_list, alpha=0.5, color="#8ecae6", linewidth=0)
plt.errorbar(samples, mean_list, std_list, fmt="o")

plt.show()
```

## Evidence
![](/Assets/Quiz027_Evidence.jpg)

*Fig.1* **Screenshot showing the result of the program**

## Part B
Convert the following RGB Color to Hex Color: (250,100,10)

![](/Assets/Quiz027_PartB.jpeg)

*Fig.2* **Workings for Part B**


