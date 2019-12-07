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
    while range < len(characters) - 3:
        four_characters = characters[range:range+4]
        opcode = four_characters[0]
        if opcode == '1':
            characters = addition(four_characters, characters)
        elif opcode == '2':
            characters = multiplication(four_characters, characters)
        elif opcode == '99':
            return characters
        range += 4



    #return characters



# Read File + main program
def main_program(inputFile):
    with open(inputFile) as file:
        pass


print(calculator_case("1,9,10,3,2,3,11,0,99,30,40,50"))
print(calculator_case("1,0,0,0,99"))
print(calculator_case("2,4,4,5,99,0"))
print(calculator_case("1,1,1,4,99,5,6,0,99"))
