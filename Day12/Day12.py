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


def count_number_of_steps(moons):
    number_of_steps = 0
    while True:
        total_velocity = 0
        apply_gravity(moons)
        apply_velocity(moons)
        for moon in moons:
            for i in range(3):
                total_velocity += moon.velocity[i]
        if total_velocity == 0:
            return number_of_steps
        number_of_steps += 1

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

Io = Moon([-1, 0, 2])
Europa = Moon([2, -10, -7])
Ganymede = Moon([4, -8, 8])
Callisto = Moon([3, 5, -1])
moons = [Io, Europa, Ganymede, Callisto]
print(count_number_of_steps(moons))
#run_number_of_steps(moons, 1000)
#print(calculate_energy(moons))

