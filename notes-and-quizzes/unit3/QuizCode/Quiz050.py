#2023-02-28 Quiz050
class flights():
    def __init__(self, flight_num, origin, destination, departure,duration):
        self.flight_num = flight_num
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.duration = duration
    def get_duration(self):
        return f"{self.duration[0]} hours {self.duration[1]} minutes and {self.duration[2]} seconds"

JL026 = flights("JL026", "HKG", "NRT", "2021-01-01 12:00:00", (5, 30, 0))
print(JL026.get_duration())

BA032 = flights("BA032", "HKG", "LHR", "2021-01-01 12:00:00", (11, 30, 0))
print(BA032.get_duration())



