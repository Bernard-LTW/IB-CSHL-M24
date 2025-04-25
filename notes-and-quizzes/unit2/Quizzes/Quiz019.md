# Quiz 019

## Prompt
Create a function that changes the vowels in a string to numbers such as a=4,e=3,i=1,o=0 and space by _


HL: Libraries or methods not allowed for this quiz. You can use dictionaries.

## Code Structure 
```.py
#2022-10-28 Quiz 019

#Create a function that changes the vowels in a string to numbers such as a=4 e=3 i=1 o=0 and the space by "_"

dict = {"a":"4", "e":"3", "i":"1", "o":"0", " ":"_"}
def get_l3tt3r(l3tt3r):
    output = ""
    for i in l3tt3r:
        if i in dict:
            output = output + dict[i]
        else:
            output = output + i

    return output


msg = "Hello World"
print(get_l3tt3r(msg))
msg = "Why did I choose CS?"
print(get_l3tt3r(msg))
msg = "Remeber the Figure Caption"
print(get_l3tt3r(msg))
```

## Evidence
![](/Assets/Quiz019_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the program**

## Part B: Boolean Circuit for:
AB + not(B+C) + B(notC notA)

![](/Assets/Quiz019_Boolean.jpg)
*Fig.2* **Boolean circuit of given equation**

