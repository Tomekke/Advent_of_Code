#Puzzle input range is 153517-630395

def is_two_same_digit(number):
    splitted_number = [int(i) for i in str(number)]
    i = 1
    while i < len(splitted_number):
        if splitted_number[i-1] == splitted_number[i]:
            return True
        i += 1
    return False

def is_two_same_digit_day2(number):
    splitted_number = [int(i) for i in str(number)]
    dic_of_numbers = {}
    for num in splitted_number:
        if num in dic_of_numbers:
            dic_of_numbers[num] += 1
        else:
            dic_of_numbers[num] = 1
    if 2 in dic_of_numbers.values():
        return True
    else:
        return False


def is_never_decreasing(number):
    string_number = str(number)
    if string_number == ''.join(sorted(string_number)):
        return True
    else:
        return False

def count_number_of_hits():
    number_of_hits = 0
    for i in range(153517, 630395):
        #Day1
        #if is_two_same_digit(i) & is_never_decreasing(i):
        #Day2
        if is_never_decreasing(i) & is_two_same_digit_day2(i):
            number_of_hits += 1
    return number_of_hits


print(count_number_of_hits())
#print(is_two_same_digit_day2(345556))

