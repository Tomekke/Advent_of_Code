class Planet:
    def __init__(self, name, depth_in_orbits):
        self.name = name
        self.satellites = {}
        self.string_of_satellites = ''
        self.depth_in_orbits = depth_in_orbits

    def add_satellite(self, satellite):
        self.satellites.update({satellite.name: satellite})

    def get_satellites_string(self):
        for satellite in self.satellites.values():
            self.string_of_satellites += satellite.get_satellites_string() + '-'
        self.string_of_satellites += self.name
        return self.string_of_satellites


def fill_in_map(input, main_planet, depth):
    planet = input.split(')')[0]
    satellite = input.split(')')[1]
    if planet == main_planet.name:
        depth += 1
        main_planet.add_satellite(Planet(satellite, depth))
    else:
        for looping_satellite in main_planet.satellites.values():
            fill_in_map(input, looping_satellite, looping_satellite.depth_in_orbits)


def count_number_of_orbits(planet, number_of_orbits):
    for satellite in planet.satellites.values():
        number_of_orbits += count_number_of_orbits(satellite, satellite.depth_in_orbits)
    return number_of_orbits


def sort_input(input, input_list, return_list):
    for piece_of_list in input_list:
        if input == piece_of_list.split(')')[0]:
            return_list.append(piece_of_list)
            return_list.append(sort_input(piece_of_list[1], input_list, return_list))
    return return_list


def read_input(filename):
    sun = Planet('COM', 0)
    list_of_input = []
    return_list = []
    with open(filename) as file:
        for line in file:
            #fill_in_map(line.rstrip(), sun, sun.depth_in_orbits)
            list_of_input.append(line.rstrip())
    print(sort_input('COM', list_of_input, return_list))
    #print(sun.get_satellites_string())
    #print(count_number_of_orbits(sun, sun.depth_in_orbits))


read_input('Day6_InputFile')



