#2022-11-17 Data Science 3
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

h=[57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0]
low=[53.0, 54.0, 54.0, 52.0, 54.0, 51.0, 53.0, 53.0, 50.0, 51.0, 52.0, 53.0, 49.0, 50.0, 50.0, 49.0, 50.0, 47.0, 50.0]
high= [58.0, 60.0, 61.0, 57.0, 56.0, 58.0, 58.0, 57.0, 56.0, 55.0, 54.0, 57.0, 54.0, 56.0, 53.0, 56.0, 53.0, 55.0, 52.0]


samples = []
for i in range(len(h)):
    samples.append(i)

fig = plt.figure(figsize=(8,4))
plt.subplot(1,2,1)

plt.plot(samples, h, color="#2b2d42", label="Relative Humidity")
plt.plot(samples, low, color="#90e0ef", label="Low Temperature")
plt.plot(samples, high, color="#d90429", label="High Temperature")
plt.xlabel("Samples")
plt.ylabel("Temperature")

mean = []
standard_deviation = []
for i in range(len(h)):
    data = [h[i], low[i], high[i]]
    mean.append(np.mean(data))
    standard_deviation.append(np.std(data))

plt.subplot(1,2,2)
plt.fill_between(samples, high, low, alpha=0.5, color="#8ecae6", linewidth=0)
plt.errorbar(samples, mean, standard_deviation, fmt="o")

plt.show()