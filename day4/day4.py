import re

IS_PART1 = True
IS_DEBUG = False


def func():

    total = 0
    with open('./day4/actual-input.txt', 'r', encoding="utf8") as file:
        for line_idx, line in enumerate(file):
            [card, numbers] = line.split(': ')
            [winning_numbers_str, actual_numbers_str] = numbers.split(' | ')
            winning_numbers = [int(x) for x in re.findall('[\d]+', winning_numbers_str)]
            actual_numbers = [int(x) for x in re.findall('[\d]+', actual_numbers_str)]

            count = 0
            for actual_number in actual_numbers:
                if actual_number in winning_numbers:
                    count += 1

            increment = 1 if count == 1 else pow(2, count-1) if count > 1 else 0

            if IS_DEBUG:
                print('\n'+line.strip())
                print('Count: ' + str(increment))

            total += increment

    print(total)


func()
