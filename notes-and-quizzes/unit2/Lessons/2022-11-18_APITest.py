#Get JSON API from 192.168.6.142/readings

import requests
import json
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

url = "http://192.168.6.142/readings"

response = requests.get(url)
data = json.loads(response.text)
readings = data["readings"][0]

#Plot a graph using the values

temp_x = []
temp_y = []
hum_x = []
hum_y = []
num_temp = 0
num_hum = 0
for r in readings:
    print(r)
    if r["sensor_id"]== 1:
        num_temp += 1
        temp_x.append(num_temp)
        temp_y.append(r["value"])
    elif r["sensor_id"]== 2:
        num_hum += 1
        hum_x.append(num_hum)
        hum_y.append(r["value"])

fig = plt.figure(figsize=(8,4))
fig.suptitle("Temperature and Humidity Readings")
plt.subplot(1,2,1)
plt.plot(temp_x, temp_y, color="red", label="Temperature")
plt.xlabel("Samples")
plt.ylabel("Temperature (C)")

plt.subplot(1,2,2)
plt.plot(hum_x, hum_y, color="blue", label="Humidity")
plt.xlabel("Samples")
plt.ylabel("Humidity (%)")



plt.show()

