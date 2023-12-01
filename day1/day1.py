import re

def func ():
    with open('./day1/actual-input.txt', 'r', encoding="utf8") as file:
        total = 0
        for line in file:
            decimals = re.findall('\d', line)
            total += int(str(decimals[0]) + str(decimals[len(decimals) - 1]))
        print(total)

func()
