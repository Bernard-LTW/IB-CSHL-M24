#2022-11-11 Linear Regression
#plot the line without using np.array
import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,1.5,4,2.5,6,4,3,5.5,5,2]
y = [3,4,8,4.5,10,5,15,9,5,16,13,3]

m, b = np.polyfit(x, y, 1)
print(f"Linear Equation: y = {m:.2f}x + {b:.2f}")
x_model = []
y_model = []
for i in [1,6]:
    x_model.append(i)
    y_model.append(m*i+b)
plt.scatter(x,y)
plt.plot(x_model,y_model, color="red")
plt.title("Scatter Plot of the data")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

