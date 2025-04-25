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

for i in range(0,len(us.get_cities())-1):
    start_city= us.get_cities()[i]
    end_city = us.get_cities()[i+1]
    x = [start_city.get_location().x,end_city.get_location().x]
    y = [start_city.get_location().y,end_city.get_location().y]
    pyplot.plot(x,y, color="pink")
    print(f"Connecting city {start_city.get_name()} to {end_city.get_name()}. Distance is {start_city.dist_calc(end_city)}")

pyplot.show()

