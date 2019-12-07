def addition(instructions, array):
    input1 = int(instructions[1])
    input2 = int(instructions[2])
    output = int(instructions[3])
    array[output] = int(array[input1]) + int(array[input2])
    return array


def multiplication(instructions, array):
    input1 = int(instructions[1])
    input2 = int(instructions[2])
    output = int(instructions[3])
    array[output] = int(array[input1]) * int(array[input2])
    return array


def calculator_case(input):
    characters = input.split(',')
    range = 0
    while range < len(characters):
        four_characters = characters[range:range+4]
        opcode = four_characters[0]
        if opcode == '1':
            characters = addition(four_characters, characters)
        elif opcode == '2':
            characters = multiplication(four_characters, characters)
        elif opcode == '99':
            break
        range += 4
    return characters



# Read File + main program
def main_program(inputFile):
    with open(inputFile) as file:
        for line in file:
            return calculator_case(line)


print(main_program('Day2_InputFile'))
