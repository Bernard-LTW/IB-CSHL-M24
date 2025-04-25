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