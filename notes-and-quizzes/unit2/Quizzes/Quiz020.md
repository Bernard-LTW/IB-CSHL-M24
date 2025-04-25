# Quiz 020

## Prompt
Create a function that produces the table of Truth for 3 inputs


HL: Truth table and circuit for:
Light = S1S2+(S2+S3(notS1))S1

## Code Structure 
```.py
#2022-11-01 Quiz 020

#Prompt: Create a function that produces the table of Truth for 3 inputs


def table_of_truth():
    print(f"|  A  |  B  |  C  |")
    for i in range(8):
        a = i//4
        b = (i%4)//2
        c = i%2
        print(f"|  {a}  |  {b}  |  {c}  |")

table_of_truth()
```

## Evidence
![](/Assets/Quiz020_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the program**

## HL Part
![](/Assets/Quiz020_Boolean.jpg)

*Fig.2* **Boolean circuit of given equation**

| S1  | S2  | S3  | Output |
|-----|-----|-----|--------|
| 0   | 0   | 0   | F      |
| 0   | 0   | 1   | F      |
| 0   | 1   | 0   | F      |
| 0   | 1   | 1   | F      |
| 1   | 0   | 0   | F      |
| 1   | 0   | 1   | F      |
| 1   | 1   | 0   | T      |
| 1   | 1   | 1   | T      |

*Table.1* **Truth Table for given equation**
