import re
from math import lcm

IS_DEBUG = False


def func():

    network = {}
    instruction = None
    keys = []
    with open('./day8/actual-input.txt', 'r', encoding="utf8") as file:

        for idx, line in enumerate(file):
            if idx == 0:
                instruction = [1 if x == 'R' else 0 for x in list(line.strip())]
            elif idx == 1:
                pass
            else:
                pattern = re.compile(r'[\w]+')

                [index, left, right] = re.findall(pattern, line)
                network[index] = {0: left, 1: right}

                if index[2] == 'A':
                    keys.append(index)

    found_idx = []
    for idx, _ in enumerate(keys):

        steps = 0
        while keys[idx][2] != 'Z':

            direction = instruction[steps % len(instruction)]
            result = network[keys[idx]][direction]

            if IS_DEBUG:
                print('Key (' + keys[idx] + ') is moving, ' + ('R' if direction == 1 else 'L') + ' to: ' + result)

            steps += 1
            keys[idx] = result

        found_idx.append(steps)

    print(lcm(*found_idx))


func()
