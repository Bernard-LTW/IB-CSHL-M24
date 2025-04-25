# Quiz 034

## Prompt
Create a new Python function called to_roman(num) that takes a single integers input.
it returns a string representing the Roman numeral equivalent of the input number.

Conditions: The function should only work for integers below 100.
If the input is greater than 100,
raise a ValueError with a message indicating that the input must be less than or equal to 100.

## Code Structure 
```.py
#2023-01-12 Quiz 034
#Create a function thta takes single integer to roman number

def to_roman(num:int)->str:
    if num > 100:
        raise ValueError("Input must me less than or equal to 100")
    #Convert int to roman number
    roman = ""
    if num == 100:
        roman = "C"
        num = 0
    if num >= 90:
        roman += "XC"
        num -= 90
    if num >= 50:
        roman += "L"
        num -= 50
    if num >= 40:
        roman += "XL"
        num -= 40
    if num >= 10:
        roman += "X" * (num // 10)
        num %= 10
    if num >= 9:
        roman += "IX"
        num -= 9
    if num >= 5:
        roman += "V"
        num -= 5
    if num >= 4:
        roman += "IV"
        num -= 4
    if num >= 1:
        roman += "I" * num
    return roman


print(to_roman(44))
```

## Evidence
![](/Assets/Quiz034_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the testing**