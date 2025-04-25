# Quiz 035

## Prompt
Create a python class for a Bank Office that follows the UML diagram on the slides
and passes the test file test_quiz35.py
## Code Structure 
```.py
#2023-01-13 Quiz 035
import random
class Account:
    def __init__(self):
        self.balance = 0
        self.holder_name = ""
        self.holder_email = ""
        number1 = random.randint(100,999)
        number2 = random.randint(10000,99999)
        number3 = random.randint(0,9)
        self.number = [f"{number1}-{number2}-{number3}"]

    def get_account_no(self):
        return self.number[0]

    def set_holder_name(self,name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.holder_name = name
        temp = f"Holder's name set to {self.holder_name}"
        return temp

    def set_holder_email(self,email):
        self.holder_email = email
        temp = f"Holder's email set to {self.holder_email}"
        return temp

    def get_balance(self):
        return self.balance

    def deposit(self,amount:int):
        self.balance += amount
        temp = f"New balance: {self.balance} USD"
        return temp
```

## Evidence
![](/Assets/Quiz035_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the testing**