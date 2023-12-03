import re

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14

}


def is_game_possible(cubes: list[str]):
    for cube in cubes:
        [quantity, color] = cube.strip().split(' ')
        if int(quantity) > int(max_cubes[color]):
            return False
    return True


def func():

    with open('./day2/actual-input.txt', 'r', encoding="utf8") as file:
        total = 0

        for line in file:
            is_possible = True
            [game_id, all_games] = line.split(': ')
            games = all_games.split(';')

            for game in games:
                cubes = game.split(',')

                if not is_game_possible(cubes):
                    is_possible = False
                    break

            if is_possible:
                total += int(re.findall('(?:[\d]+)', game_id)[0])

        print(total)


func()
