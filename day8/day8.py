import re

IS_DEBUG = False


def func():

    network = {}
    instruction = None
    with open('./day8/actual-input.txt', 'r', encoding="utf8") as file:

        for idx, line in enumerate(file):
            if idx == 0:
                instruction = [1 if x == 'R' else 0 for x in list(line.strip())]
            elif idx == 1:
                pass
            else:
                pattern = re.compile(r'[A-Z]+')

                [index, left, right] = re.findall(pattern, line)
                network[index] = {0: left, 1: right}

    steps = 0
    key = 'AAA'

    while key != 'ZZZ':

        direction = instruction[steps % len(instruction)]
        result = network[key][direction]

        if IS_DEBUG:
            print('Key (' + key + ') is moving, ' + ('R' if direction == 1 else 'L') + ' to: ' + result)

        steps += 1
        key = result

    print(steps)


func()
