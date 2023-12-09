import re
import math

IS_PART1 = True
IS_DEBUG = False


def func():

    with open('./day6/actual-input.txt', 'r', encoding="utf8") as file:

        races = []
        for line_idx, line in enumerate(file):

            vals = [int(x) for x in re.findall('[\d]+', line)]

            if line_idx == 0:
                for _ in range(len(vals)):
                    races.append({'time': None, 'distance': None})

            key = 'time' if line_idx == 0 else 'distance'

            for idx, val in enumerate(vals):
                races[idx][key] = val

    counters = [0] * len(races)
    for idx, race in enumerate(races):
        for ms in range(race['time']):
            if (ms * (race['time'] - ms)) > race['distance']:
                counters[idx] += 1

    print(math.prod(counters))


func()
