#Build a coin toss simulator

import random

def CTS(x,y):
    heads = 0
    tails = 0
    for i in range(x):
        toss = random.random()
        if toss > y:
            heads = heads + 1
        else:
            tails = tails + 1
    return f"Number of heads: {heads}, Number of tails: {tails}"

for i in range(10):
    print(CTS(100,0.5))



