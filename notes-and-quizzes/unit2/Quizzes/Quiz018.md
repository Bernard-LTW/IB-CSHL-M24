# Quiz 018

## Prompt
### Create a function to help Lily

Lily was crossing a forest when she realizes that there is a tiger ahead of her who has seen Lily.
Lily quickly takes out a matchbox from her bag and burns a matchstick, because the tiger is afraid of fire.

A matchstick takes 5 seconds to burn completely.  The length of the forest that Lily needs to cross is "l" meters. Lily's speed is s cm/s

What is the minimum number of matchsticks Lily needs to burn to cross the forest safely?

| Input l:int s:int | Output:int   |
|-------------------|--------------|
| 100, 100          | 20 matches   |
| 250, 110          | 46 matches   |
| 500, 150          | 67 matches   |
| 12345, 123        | 2008 matches |



HL: Create the Truth table for the boolean equation

out = ABC+(A+B+C)+not(notA notB notC)

![](/Assets/Quiz018_Boolean.jpeg)

| Input | Output |
|-------|--------|
| 0 0 0 | 0      |
| 0 0 1 | 1      |
| 0 1 0 | 1      |
| 0 1 1 | 1      |
| 1 0 0 | 1      |
| 1 0 1 | 1      |
| 1 1 0 | 1      |
| 1 1 1 | 1      |


## Code Structure 
```.py
#Quiz 018 2022-10-27

#Version with Math
import math
def numberMatches(l,s):
    return f"{math.ceil(20*l/s)} matches"
print("With Math")
print(numberMatches(100, 100))
print(numberMatches(250, 110))
print(numberMatches(500, 150))
print(numberMatches(12345, 123))

#Version without Math
def numberMatchesNM(l,s):
    l = 20*l
    sum = 0
    while l > 0:
        l = l-s
        sum = sum+1
    return f"{sum} matches"


print("Without Math")
print(numberMatchesNM(100, 100))
print(numberMatchesNM(250, 110))
print(numberMatchesNM(500, 150))
print(numberMatchesNM(12345, 123))
```

## Evidence
![](/Assets/Quiz018_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the program**