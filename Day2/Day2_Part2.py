import random

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
    characters = input
    range = 0
    while range < len(characters):
        opcode = characters[range]
        if opcode == '1':
            four_characters = characters[range:range + 4]
            characters = addition(four_characters, characters)
            range += 4
        elif opcode == '2':
            four_characters = characters[range:range + 4]
            characters = multiplication(four_characters, characters)
            range += 4
        elif opcode == '99':
            break
    return characters


def replace_content(input):
    noun_end_range = 100
    verb_end_range = 100
    for noun in range(0, noun_end_range):
        for verb in range(0, verb_end_range):
            modified_input = input.split(',')
            if noun < len(modified_input):
                if verb < len(modified_input):
                    modified_input[1] = noun
                    modified_input[2] = verb
                    if calculator_case(modified_input)[0] == 19690720:
                        return modified_input
                else:
                    verb = verb_end_range
            else:
                noun = noun_end_range


# Read File + main program
def main_program(inputFile):
    with open(inputFile) as file:
        for line in file:
            output = replace_content(line)
            return 100*output[1] + output[2]


print(main_program('Day2_InputFile'))
#print(replace_content('1,0,0,0'))