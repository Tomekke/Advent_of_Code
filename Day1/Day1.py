import math

def calculate_fuel(mass):
    return math.floor(mass/3) - 2

def sum_of_masses(input_file):
    with open(input_file) as file:
        sum_of_fuel=0
        for line in file:
            sum_of_fuel += calculate_fuel(int(line))
    return sum_of_fuel

print(sum_of_masses('Day1_InputFile'))