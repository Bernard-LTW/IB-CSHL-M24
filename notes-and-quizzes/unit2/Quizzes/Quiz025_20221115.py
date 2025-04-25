#2022-11-15 Quiz 025
#Prompt: Create a program that shows the graph of the function below for 100 values of x in the interval -10<x<10

from matplotlib import pyplot as plt

x_list = []
y_list = []

for x in range(-50,50):
    x /= 5
    x_list.append(x)
    y_list.append(abs(x))

plt.plot(x_list, y_list, color="red")
plt.show()