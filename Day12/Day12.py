class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]


def apply_gravity(moons):
    x = 1
    for moon in moons:
        for y in range(x, len(moons)):
            for i in range(3):
                if moon.position[i] < moons[y].position[i]:
                    moon.velocity[i] += 1
                    moons[y].velocity[i] -= 1
                elif moon.position[i] > moons[y].position[i]:
                    moon.velocity[i] -= 1
                    moons[y].velocity[i] += 1
        x += 1


def apply_velocity(moons):
    for moon in moons:
        for i in range(3):
            moon.position[i] += moon.velocity[i]


def count_number_of_steps(moon, moons, coordinates):
    initial_coordinates = coordinates
    number_of_steps = 1
    while True:
        apply_gravity(moons)
        apply_velocity(moons)
        number_of_steps += 1
        if tuple(initial_coordinates) == tuple(moon.position):
            return number_of_steps



#Day1 function
def run_number_of_steps(moons, steps):
    i = 0
    while i < steps:
        apply_gravity(moons)
        apply_velocity(moons)
        i += 1

#Day1 function
def calculate_energy(moons):
    total_energy = 0
    for moon in moons:
        potential_energy = 0
        kinetic_energy = 0
        for i in range(3):
            potential_energy += abs(moon.position[i])
            kinetic_energy += abs(moon.velocity[i])
        total_energy += potential_energy * kinetic_energy
    return total_energy

Io = Moon([-8, -10, 0])
Europa = Moon([5, 5, 10])
Ganymede = Moon([2, -7, 3])
Callisto = Moon([9, -8, -3])
moons = [Io, Europa, Ganymede, Callisto]
print(count_number_of_steps(Io, moons, [-8, -10, 0]))
#print(count_number_of_steps(Europa, moons, [5, 5, 10]))
#print(count_number_of_steps(Ganymede, moons, [2, -7, 3]))
#print(count_number_of_steps(Callisto, moons, [9, -8, -3]))
#run_number_of_steps(moons, 2772)
#print(Europa.position)
#print(calculate_energy(moons))

