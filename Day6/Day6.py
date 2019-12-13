class Planet:
    def __init__(self, name):
        self.name = name
        self.satellites = {}
        self.string_of_satellites = ''

    def add_satellite(self, satellite):
        self.satellites.update({satellite.name: satellite})

    def get_satellites_string(self):
        for satellite in self.satellites.values():
            self.string_of_satellites += satellite.get_satellites_string()
        self.string_of_satellites += self.name
        return self.string_of_satellites


def fill_in_map(input):
    planet = input.split(')')[0]
    satellite = input.split(')')[1]
    if planet == sun.name:
        sun.add_satellite(Planet(satellite))
    else:
        sun.satellites[planet].add_satellite(Planet(satellite))


def read_input(filename):
    with open(filename) as file:
        for line in file:
            fill_in_map(line.rstrip())


sun = Planet('COM')
read_input('Day6_TestFile')
print(sun.get_satellites_string())


