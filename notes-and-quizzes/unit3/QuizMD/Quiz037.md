# Quiz 037

## Prompt

An accounting firm needs a software package to calculate compound interest. Draw the UML diagram.

### Classes Description

A CompoundInterest class is used to calculate the compound interest of a given principal, rate and number of years with
the equation principal * (1 + rate) ** years

There is an AccountingProgram class that uses composition to include an object of the CompoundInterest class, which it uses to perform the interest calculation. The AccountingProgram class provides a set of methods to set the principal, rate and years, and a calculate_interest
method that gets the compound interest by calling the calculate method of the compound_interest_calculator object

## Code Structure

```.py
#2023-01-19 Quiz 037

class CompoundInterest:
    def __init__(self,principal:int, rate:float, year:int):
        self.principal = principal
        self.rate = rate
        self.year = year


class AccountingProgram:
    def __init__(self):
        self.compound = CompoundInterest(0,0,0)
    def set_principal(self,principal):
        if principal <= 0:
            raise ValueError("Principal should be greater than zero")
        self.compound.principal = principal
        return f"Principal set to {self.compound.principal}"

    def set_rate(self,rate):
        if rate <= 0:
            raise ValueError("Interest rate should be greater than zero")
        self.compound.rate = rate
        return f"Rate set to {self.compound.rate}"

    def set_years(self, year):
        if year <= 0:
            raise ValueError("Years should be greater than zero")
        self.compound.year = year
        return f"Year set to {self.compound.year}"

    def calculate_interest(self):
        temp = self.compound.principal*(1+self.compound.rate)**self.compound.year
        format_float = "{:.2f}".format(temp)
        return float(format_float)
```

## Evidence

![](/Assets/Quiz037_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the testing**

## UML Diagram

![](/Assets/Quiz037_UML.jpeg)
*Fig.2* **UML Diagram of Classes**