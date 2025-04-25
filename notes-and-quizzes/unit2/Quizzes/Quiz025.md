# Quiz 025

## Part A Prompt
Create a program that shows the graph of the function below for 100 values of x in the interval $-10 < x < 10$
## Code Structure 
```.py
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
```

## Evidence
![](/Assets/Quiz025_Evidence.jpg)

*Fig.1* **Screenshot showing the result of the program**

## Part B
Convert to decimal: FFA5

$(FFA5)₁₆ = (15 × 16³) + (15 × 16²) + (10 × 16¹) + (5 × 16⁰) = (65445)₁₀$


