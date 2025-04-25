import random
from matplotlib import pyplot
random.seed(0)
class Coordinate:
    def __init__(self,x,y):
        self.x:float = x
        self.y:float = y
    def __repr__(self):
        return f"Coordinate({self.x},{self.y})"
class City:
    def __init__(self,name:str,location:Coordinate):
        self.name = name
        self.location = location
    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def dist_calc(self,city):
        return ((self.location.x - city.location.x)**2 + (self.location.y - city.location.y)**2)**0.5

    def __repr__(self):
        return f"City({self.name},{self.location})"

class country:
    def __init__(self, name:str, capital:City):
        self.name = name
        self.cities = []
        self.capital = capital

    def new_city(self,city:City):
        if city in self.cities:
            raise ValueError("City already exists")
        if not isinstance(city,City):
            raise ValueError("City must be a City object")
        self.cities.append(city)
    def get_capital(self):
        return self.capital
    def get_cities(self):
        return self.cities


us_city_name = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose"]

us_capital = City("Washington DC",Coordinate(38.8951,-77.0367))
us = country("United States",us_capital)

for name in us_city_name:
    city = City(name,Coordinate(random.randint(0,100),random.randint(0,100)))
    us.new_city(city)

#print(us.get_capital())
#print(us.get_cities())

#Homework 0117
#Create 10 random cities in a unit-3 smart way
#Create a method in the class city that recieves as input another city and returns the distance between them
#3-500 original characters: What is the salesman problem and possible solutions?

"""
The salesman needs to transport lemon tea over states. He needs to calculate the shortest distance in between states and also the shortest path one should take. The way to calculate the distance between points and compare is to write a program to find out the line distances between points and sort them accordingly.
"""


#Homework 0118
#Calculate the distance between the captial and all cities in the country

for city in us.get_cities():
    temp = us.get_capital().dist_calc(city)
    format_float = "{:.2f}".format(temp)
    print(f"Distance between {us.get_capital().get_name()} and {city.get_name()} is {format_float}")

