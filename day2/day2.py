import re
from functools import reduce

MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

CUBE_INDEX = {
    'red': 0,
    'green': 1,
    'blue': 2
}

IS_PART1 = False


def is_game_possible(cubes: list[str]):
    for cube in cubes:
        [quantity, color] = cube.strip().split(' ')
        if int(quantity) > int(MAX_CUBES[color]):
            return False
    return True


def func():

    with open('./day2/actual-input.txt', 'r', encoding="utf8") as file:
        total = 0

        for line in file:
            is_possible = True
            [game_id, all_games] = line.split(': ')
            games = all_games.split(';')
            minimum = [0, 0, 0]

            for game in games:
                cubes = game.split(',')

                if IS_PART1:
                    if not is_game_possible(cubes):
                        is_possible = False
                        break
                else:
                    for cube in cubes:
                        [quantity, color] = cube.strip().split(' ')
                        if minimum[CUBE_INDEX[color]] < int(quantity):
                            minimum[CUBE_INDEX[color]] = int(quantity)

            if IS_PART1:
                if is_possible:
                    total += int(re.findall('(?:[\d]+)', game_id)[0])
            else:
                total += reduce(lambda x, y: x*y, minimum)

        print(total)


func()
