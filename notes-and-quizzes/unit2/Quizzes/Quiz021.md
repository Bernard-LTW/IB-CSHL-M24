# Quiz 021

## Prompt
Using the function that produces the table of Truth for 3 inputs, add a column for the boolean equation
Equation: AB + (not B) + (not B C)

HL: Truth table and circuit for:
X = ZW + (Z+Y(not W))

## Code Structure 
```.py
#2022-11-04 Quiz 021
#Build a function that produces the truth tabel for 3 inputs and add a column for the boolean equation : AB+(not B)+(notB C)

def table_of_truth_equation():
    print(f"|  A  |  B  |  C  | AB + not B + not CB |")
    for i in range(8):
        a = i//4
        b = (i%4)//2
        c = i%2
        d = int(a and b) or int(not b) or int(not b and c)
        print(f"|  {a}  |  {b}  |  {c}  |          {d}          |")

table_of_truth_equation()
```

## Evidence
![](/Assets/Quiz021_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the program**

## HL Part
![](/Assets/Quiz021_Boolean.jpg)

*Fig.2* **Boolean circuit of given equation**

| S1  | S2  | S3  | Output |
|-----|-----|-----|--------|
| 0   | 0   | 0   | F      |
| 0   | 0   | 1   | T      |
| 0   | 1   | 0   | T      |
| 0   | 1   | 1   | T      |
| 1   | 0   | 0   | F      |
| 1   | 0   | 1   | T      |
| 1   | 1   | 0   | F      |
| 1   | 1   | 1   | T      |

*Table.1* **Truth Table for given equation**
