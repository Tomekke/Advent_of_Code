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


def run_number_of_steps(moons, steps):
    i = 0
    while i < steps:
        apply_gravity(moons)
        apply_velocity(moons)
        i += 1


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

Io = Moon([15, -2, -6])
Europa = Moon([-5, -4, -11])
Ganymede = Moon([0, -6, 0])
Callisto = Moon([5, 9, 6])
moons = [Io, Europa, Ganymede, Callisto]
run_number_of_steps(moons, 1000)
print(calculate_energy(moons))

