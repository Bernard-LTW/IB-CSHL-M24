# Quiz 033

## Prompt
Write the function mystery and pass the tests contained in the file Quiz033_Test.py

The function takes two lists, list1 and list2, as input and creates an empty list called output.
It then iterates over the elements of list1 using a loop,
and for each element, it iterates over the elements of list2 using another loop.
For each pair of elements, the function checks if the two elements are equal.
If they are, it adds the elements from list1 to the output list.
After both loops have completed, the function returns the output list.

## Code Structure 
```.py
#2023-01-10 Quiz 033

def mystery(list1, list2:list):
    output = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                output.append(list1[i])
    return output
```

## Evidence
![](/Assets/Quiz033_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the testing**