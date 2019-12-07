#Puzzle input range is 153517-630395

def is_two_same_digit(number):
    splitted_number = [int(i) for i in str(number)]
    i = 1
    while i < len(splitted_number):
        if splitted_number[i-1] == splitted_number[i]:
            return True
        i += 1
    return False



def is_never_decreasing(number):
    string_number = str(number)
    if string_number == ''.join(sorted(string_number)):
        return True
    else:
        return False


number_of_hits = 0
for i in range(153517, 630395):
    if is_two_same_digit(i) & is_never_decreasing(i):
        number_of_hits += 1
print(number_of_hits)

