# Quiz 029

## Part A Prompt
Create a function that receives a dictionary with letters in the alphabet as keys and a string. The functions returns the dictionary with a count as value for the occurrence of each letter:

## Code Structure 
```.py
#2022-11-29 Quiz 029

#Create a function that receives a dictionary with letters in the alphabet as keys and a string. The functions returns the dictionary with a count as value for the occurrence of each letter:

dict = {'w':0, 'l':0,'c':0}
dict2 = {'a':0, 'e':0,'i':0, 'o':0, 'u':0}

def count_letters(my_dict, string):
    for i in string:
        if i in my_dict:
            my_dict[i] += 1
    return my_dict

print(count_letters(dict, "hello world"))

print(count_letters(dict2, "Why did I choose CS?"))
```

## Evidence
![](/Assets/Quiz029_Evidence.jpg)

*Fig.1* **Screenshot showing the result of the program**

## Part B
How many different colors could you represent in a 6 bit computer?
Systems with a 6-bit RGB palette use 2 bits for each of the red, green, and blue color components. This results in a $(2^2)^3=4^3=64$-color palette.

“List of Monochrome and RGB Color Formats.” Wikipedia, Wikimedia Foundation, 18 Nov. 2022, https://en.wikipedia.org/wiki/List_of_monochrome_and_RGB_color_formats#6-bit_RGB. 





