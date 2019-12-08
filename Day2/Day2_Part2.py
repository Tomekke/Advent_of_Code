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


def calculator_case(characters):
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


def replace_content(input):
    static_read_input = input
    noun = 50
    verb = 50
    while True:
        changing_input = static_read_input
        changing_input[1] = noun
        changing_input[2] = verb
        output = calculator_case(changing_input)[0]
        if output == 19690720:
            return changing_input
        elif output > 19690720:
            noun = noun/2
            verb = verb/2
        elif output < 19690720:
            noun = noun * 1.5
            verb = verb * 1.5

# Read File + main program
def main_program(inputFile):
    with open(inputFile) as file:
        for line in file:
            return replace_content(line.split(','))


print(main_program('Day2_InputFile'))
