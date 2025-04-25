# Quiz 026

## Part A Prompt
Create a program that shows the graph of the data and create a linear (H_model = m*h + b) model for the data.

## Code Structure 
```.py
#2022-11-17 Quiz 026
#Prompt: Create a program that shows the graph of the data and create a linear (H_model = m*h + b) model for the data.

h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]
samples = []

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("dark_background")
for i in range(len(h)):
    samples.append(i)

plt.plot(samples, h, linestyle="None", marker="v")
plt.xlabel("Samples")
plt.ylabel("Relative Humidity")

m, b = np.polyfit(samples, h, 1)
print(f"Linear Equation: y = {m:.2f}h + {b:.2f}")
h_model = []
y_model = []
for i in [1,32]:
    h_model.append(i)
    y_model.append(m*i+b)
plt.plot(h_model,y_model, color="red")
plt.text(5, 55.5, f"y = {m:.2f}h + {b:.2f}")

plt.show()
```

## Evidence
![](/Assets/Quiz026_Evidence.jpg)

*Fig.1* **Screenshot showing the result of the program**

## Part B
Convert the following color in hex to rgb: #e6e627

$(e6e627)₁₆ = (14 × 16¹) + (6 × 16⁰) + (14 × 16¹) + (6 × 16⁰) + (2 × 16¹) + (7 × 16⁰) = (230, 230, 39)₁₀$

![](/Assets/Quiz026_PartB.jpg)

*Fig.2* **Workings for Part B**


