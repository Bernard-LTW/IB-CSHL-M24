#2022-11-15 Predictions
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


#prediction for x = 7 (Extrapolation)
y_x_7 = m*7+b
print(f"Prediction for x = 7: {y_x_7:.2f}")
plt.plot([7],[y_x_7], "b+")
plt.text(5.5,17, f"Prediction for x = 7: {y_x_7:.2f}")

#prediction for x = 4.5 (Extrapolation)
y_x_4half = m*4.5+b
print(f"y(x) = {y_x_4half:.2f}")
plt.plot([4.5],[y_x_4half], "g+")
plt.text(4.25,9.25, f"y(4.5) = {y_x_4half:.2f}")

plt.show()