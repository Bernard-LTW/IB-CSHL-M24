# Quiz 038

## Prompt
Create the Salesman Map with OOP structure

## Code Structure

```.py
#2023-01-20 Quiz 038
from matplotlib import pyplot
import random
from Lessons.composition_travelling_salesman import City, Coordinate,country

pyplot.style.use("ggplot")

us_city_name = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose"]

us_capital = City("Washington DC",Coordinate(38.8951,-77.0367))
us = country("United States",us_capital)

for name in us_city_name:
    city = City(name,Coordinate(random.randint(0,100),random.randint(0,100)))
    us.new_city(city)


#Plot the coordinates
x = []
y = []
labels = []
for city in us.get_cities():
    x.append(city.location.x)
    y.append(city.location.y)
    labels.append(city.name)
pyplot.scatter(x,y,s=100)
for i, label in enumerate(labels):
    pyplot.annotate(label,(x[i],y[i]))
pyplot.title("Salesman Map")
pyplot.show()
```

## Evidence

![](/Assets/Quiz038_Evidence.jpg)
*Fig.1* **Image showing plotted graph**