# Quiz 017

## Prompt
Create a function that produces the average word length of the input list

## Code Structure 
```.py
#2022-10-25 Quiz 017
#Create a function that produces the average word length of the input list


def averageLength():
     return sum([len(i.strip()) for i in stringList])/len(stringList)
stringList = ["Hello", "main"]
print(averageLength())
```

## Evidence
![](/Assets/Quiz017_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the program**