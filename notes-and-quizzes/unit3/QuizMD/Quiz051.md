# Quiz 051

## Prompt
Create a Bicycle class with a wheel class as its attribute using composition.

The bicycle class should have a ride() method that returns a string with the frame and wheel size.
The Wheel class should have a get_size() method that returns the size of the wheel,
as well as a get_perimeter() method that returns the perimeter of the wheel and a get_rotation_per_km() method that returns the number of rotations the wheel makes per km.

Create an object for a bicycle with wheel size 26 and frame aluminum. How many rotations does the wheel make per km?
## Code Structure

### Python File
```python
#2023-03-02 Quiz 051

class Wheel:
    def __init__(self, size):
        self.size = size
        self.cm = self.size * 2.54
    def get_size(self):
        return self.size

    def get_rotation_per_km(self):
        return 100000 / self.cm / 3.14

    def get_perimeter(self):
        return round(self.size / 2 * 3.14)
class Bicycle:
    def __init__(self, frame, wheels):
        self.frame = frame
        self.wheels = Wheel(wheels)

    def __str__(self):
        return "Bicycle: frame = " + self.frame + ", wheels = " + str(self.wheels)

    def ride(self):
        return f"Riding a bicycle with {self.wheels.get_size()} inch wheels and a {self.frame} frame."


BikeA = Bicycle("Aluminium", 26)
print(BikeA.ride())
print(f"The perimeter of the wheel is {BikeA.wheels.get_perimeter()} inches.")
print(f"The rotation per km is {round(BikeA.wheels.get_rotation_per_km())}.")
```

## Evidence

![](/Assets/Quiz051_Evidence.jpg)
*Fig.1* **Image showing output of program**

