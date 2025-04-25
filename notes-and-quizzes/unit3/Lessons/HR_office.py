class Employee:
    def __init__(self, name, email, position, age, salary):
        self.name = name
        self.email = email
        self.position = position
        self.age = age
        self.salary = salary

    def greet(self):
        temp = f"Hello {self.name}, you are {self.age} years old and work as a {self.position} in our company.Your email address is {self.email}"
        return temp

emp1 = Employee(name="frank murphy", email = "frank.murphy@company.xy",position = "Driver",age = "39",salary = "29000")
emp2 = Employee(name="jane smith", email = "jane.smith@hercompany.ha", position="Programmer", age="22", salary="15000")

#emp3 = ["elon musk", "elon.musk@twitter.inc","CEO", "45", "1000000"]
#emp4 = ["bill gates", "bill.gates@microsoft.com", "CTO", "55", "1000000"]
#emp5 = ["steve jobs", "steve.jobs@icloud.com", "Dead", "65", "0"]

database = [emp1, emp2]

for employee in database:
    print(employee.greet())
    print(employee.email)