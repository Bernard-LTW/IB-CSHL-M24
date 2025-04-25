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
