class Pet:
    def __init__(self, name:str,price:int, type:str):
        self.name = name
        self.type = type
        self.price = price
        print("Created a pet")

    def get_price_tax(self):
        return self.price*1.1

class Goldfish(Pet):
    def __init__(self, brain:bool, name:str, price:int):
        super().__init__ (name=name, price=price, type = "fish")
        self.brain = brain
        print("Created a Goldfish")

    def swim(self):
        return "Swimming straight" if self.brain else "Swimming upside down"

#Create a new pet
bob = Pet(name="Bob", price=3, type="dog")
print(bob.get_price_tax())
carl = Goldfish(name="carl",price = 5, brain=True)
print(carl.swim())