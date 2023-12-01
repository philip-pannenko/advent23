import re

dictionary = {
    "1": 1,
    "one": 1,
    "2": 2,
    "two": 2,
    "3": 3,
    "three": 3,
    "4": 4,
    "four": 4,
    "5": 5,
    "five": 5,
    "6": 6,
    "six": 6,
    "7": 7,
    "seven": 7,
    "8": 8,
    "eight": 8,
    "9": 9,
    "nine": 9
}


def func():
    with open('./day1/actual-input.txt', 'r', encoding="utf8") as file:
        total = 0
        for line in file:
            decimals = re.findall(
                '(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
            total += int(
                str(dictionary[decimals[0]]) +
                str(dictionary[decimals[len(decimals) - 1]])
            )
        print(total)


func()
