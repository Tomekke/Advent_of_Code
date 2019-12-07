import math

def calculate_fuel(mass):
    return math.floor(mass/3) - 2

def masses_and_fuel(mass):
    actual_mass = calculate_fuel(mass)
    if calculate_fuel(actual_mass) > 0:
        actual_mass += masses_and_fuel(actual_mass)
    return actual_mass


def sum_of_masses(input_file):
    with open(input_file) as file:
        sum_of_fuel=0
        for line in file:
            sum_of_fuel += masses_and_fuel(int(line))
    return sum_of_fuel

print(sum_of_masses('Day1_InputFile'))
#print(masses_and_fuel(100756))