
puzzleInput = open('input.txt').read().split('\n')

WRITTEN_DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


sum = 0
j = 0
for row in puzzleInput:

    string = ''
    first_digit = 0
    second_digit = 0
    lowest_index = 1000
    biggest_index = 0

    for digit in WRITTEN_DIGITS:
        i = 0
        while row.find(digit, i, len(row)) != -1:
            index = row.find(digit, i, len(row))
            if index < lowest_index and index != -1:
                first_digit = WRITTEN_DIGITS[digit]
                lowest_index = index
            if index >= biggest_index:
                second_digit = WRITTEN_DIGITS[digit]
                biggest_index = index
            i = index + 1

    for digit in DIGITS:
        i = 0
        while row.find(digit, i, len(row)) != -1:
            index = row.find(digit, i, len(row))
            if index < lowest_index and index != -1:
                first_digit = int(digit)
                lowest_index = index
            if index >= biggest_index:
                second_digit = int(digit)
                biggest_index = index
            i = index + 1


    j += 1
    string += str(first_digit)
    string += str(second_digit)
    print(f"digit{j} = {string}")
    sum += int(string)
    print(f"sum{j} = {sum}")

print(f"Total Sum = {sum}")