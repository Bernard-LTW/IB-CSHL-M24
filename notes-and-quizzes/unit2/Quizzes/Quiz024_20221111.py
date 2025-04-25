# 2022-11-11 Quiz 024

# Create a program that shows the graph of the parabola for 100 values of x in the interval of -10 to 10

# Equation: f(x) = 2(x+5)^2


from matplotlib import pyplot as plt


def produce():
    x_list = []
    y_list = []
    for i in range(100):
        x = -10 + i * 0.2
        x_list.append(x)
        y = 2 * (i + 5) ** 2
        y_list.append(y)
    return y_list, x_list


data_y, data_x = produce()

plt.plot(data_x, data_y, color="red")
plt.xlabel("x")
plt.ylabel("$y = 2(x+5)^2$")
plt.show()
