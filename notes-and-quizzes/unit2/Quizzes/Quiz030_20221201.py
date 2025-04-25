#2022-12-01 Quiz 030
#Using the data in the learning log(item 21), create a graph with a smoothed version where the smoothing window is every 4 points
#HL: Smoothing Window overlaps 50%

h=[57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0]
low=[53.0, 54.0, 54.0, 52.0, 54.0, 51.0, 53.0, 53.0, 50.0, 51.0, 52.0, 53.0, 49.0, 50.0, 50.0, 49.0, 50.0, 47.0, 50.0]
high= [58.0, 60.0, 61.0, 57.0, 56.0, 58.0, 58.0, 57.0, 56.0, 55.0, 54.0, 57.0, 54.0, 56.0, 53.0, 56.0, 53.0, 55.0, 52.0]

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

window = 4
overlap = 2
samples = []
samples_h = []
samples_low = []
samples_high = []
samples_smooth = []
count = 0

#Calculate the high mean and low for values given in the window with the overlap of 50%
for i in range(len(h)):
    samples.append(i)

for i in range(0, len(h), window//2):
    samples_smooth.append(i)
    values = h[i:i+window]
    samples_h.append(np.mean(values))


#Plot the graph
fig = plt.figure(figsize=(4,8))
plt.subplot(3,1,1)
plt.plot(samples,h)
plt.subplot(3,1,2)
plt.plot(samples_smooth, samples_h)

plt.show()




