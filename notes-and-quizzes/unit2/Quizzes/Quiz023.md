# Quiz 023

## Part A Prompt
Create a function that produces the graph for the function in Quiz 022

## Code Structure 
```.py
#2022-11-10 Quiz 023

#Create a function that produces the graph for the function in Quiz 022

from matplotlib import pyplot as plt
import random

random.seed(1234)

def produce(n,m,s):
    print(f"|    x     |   y(x)   |")
    x_list = []
    y_list = []
    for i in range(n):
        x = random.randint(0,100)
        x_list.append(x)
        y =x**(1/2*(m/s)**2)
        y_list.append(y)
        y_str = f"{y:.2f}"
        print(f"|{str(x).center(10)}|{y_str.center(10)}|")
    return y_list,x_list
data_y, data_x = produce(n=10,m=3,s=2)
plt.plot(data_x,data_y, color= "red", marker= "o")
plt.xlabel("x")
plt.ylabel("$y = x^{1/2*(m/s)^2}$")
plt.show()
```

## Evidence
![](/Assets/Quiz023_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the program**

## Part B

Truth Table for A(A+B)

| A | B | Output |
|---|---|--------|
| 0 | 0 | F      |
| 0 | 1 | F      |
| 1 | 0 | T      |
| 1 | 1 | T      |

*Table.1* **Truth Table for given equation**


