def move(coordinate, direction):
    direction_letter = direction[0]
    direction_length = int(direction[1:])
    array_of_steps = []
    if direction_letter == 'U':
        for step in range(1, direction_length + 1):
            array_of_steps.append([coordinate[0], coordinate[1] + step])
    elif direction_letter == 'R':
        for step in range(1, direction_length + 1):
            array_of_steps.append([coordinate[0] + step, coordinate[1]])
    elif direction_letter == 'D':
        for step in range(1, direction_length + 1):
            array_of_steps.append([coordinate[0], coordinate[1] - step])
    elif direction_letter == 'L':
        for step in range(1, direction_length + 1):
            array_of_steps.append([coordinate[0] - step, coordinate[1]])
    return array_of_steps


def stip_path(directions):
    steps = [[0,0]]
    for direction in directions.split(','):
        steps += (move(steps[-1], direction))
    return steps


def check_if_crossing(arrayA, arrayB):
    crossings = []
    steps_of_arrayA = stip_path(arrayA)
    steps_of_arrayB = stip_path(arrayB)
    if len(steps_of_arrayA) >= len(steps_of_arrayB):
        for step in steps_of_arrayA:
            if step in steps_of_arrayB:
                crossings.append(step)
    else:
        for step in steps_of_arrayB:
            if step in steps_of_arrayA:
                crossings.append(step)
    return crossings


def read_and_execute():
    arrayA = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    arrayB = 'U62,R66,U55,R34,D71,R55,D58,R83'
    crossings = check_if_crossing(arrayA, arrayB)
    crossings.sort()
    closest_coordinate = crossings[1]
    return closest_coordinate[0] + closest_coordinate[1]


print(read_and_execute())
#print(check_if_crossing('R8,U5,L5,D3', 'U7,R6,D4,L4'))
#print(stip_path('R8,U5,L5,D3'))
#print(stip_path('U7,R6,D4,L4'))