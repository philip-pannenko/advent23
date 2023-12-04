import re
from functools import reduce

IS_PART1 = False
IS_DEBUG = False

gear_ratio = {}


def get_gear_ratio(
        engine_schematic_xy: str,
        engine_schematic: list[str],
        adjacent_engine_schematic_xy: str,
        adjacent_engine_schematic: list[str]) -> int:
    result = 0

    if (engine_schematic is not None
        and engine_schematic[0] is not None
        and adjacent_engine_schematic is not None
            and adjacent_engine_schematic[0] is not None):

        if engine_schematic[0].isdigit():
            if adjacent_engine_schematic is not None and adjacent_engine_schematic[0] == '*':
                
                # this case is for when a gear exists directly to the left of the engine_schematic and must be added
                if not adjacent_engine_schematic_xy in gear_ratio:
                    gear_ratio[adjacent_engine_schematic_xy] = []

                gear_ratio[adjacent_engine_schematic_xy].append(
                    int(engine_schematic[0]))

                if IS_DEBUG:
                    print(
                        '\t\t adding, ' + engine_schematic[0] + ' existing gear ratio[' + adjacent_engine_schematic_xy + ']')
                
                # dereference this engine schematic so that the follow iterations,
                #  this schematic isn't double counted
                engine_schematic[0] = None

        elif engine_schematic[0] == '*':
            if adjacent_engine_schematic is not None and adjacent_engine_schematic[0].isdigit():
                if IS_DEBUG:
                    print('\t\t creating gear ratio: ' +
                          engine_schematic_xy)
                
                if not engine_schematic_xy in gear_ratio:
                    gear_ratio[engine_schematic_xy] = []

                gear_ratio[engine_schematic_xy].append(
                    int(adjacent_engine_schematic[0]))
                
                # dereference this engine schematic so that the follow iterations,
                #  this schematic isn't double counted
                adjacent_engine_schematic[0] = None
    
    return result

# compare the schematics and return an increment value


def get_adjacent_increment(engine_schematic: list[str], adjacent_engine_schematic: list[str]) -> int:
    result = 0

    if (engine_schematic is not None
        and engine_schematic[0] is not None
        and adjacent_engine_schematic is not None
            and adjacent_engine_schematic[0] is not None):

        if engine_schematic[0].isdigit():
            if adjacent_engine_schematic is not None and not adjacent_engine_schematic[0].isdigit():
                result = int(engine_schematic[0])

                # dereference this engine schematic so that the follow iterations,
                #  this schematic isn't double counted
                engine_schematic[0] = None

        elif not engine_schematic[0].isdigit():
            if adjacent_engine_schematic is not None and adjacent_engine_schematic[0].isdigit():
                result = int(adjacent_engine_schematic[0])

                # dereference this engine schematic so that the follow iterations,
                #  this schematic isn't double counted
                adjacent_engine_schematic[0] = None

    if IS_DEBUG and result != 0:
        print('\t\t adding: ' + str(result))

    return result


def func():

    with open('./day3/actual-input.txt', 'r', encoding="utf8") as file:
        total = 0
        prev_line_dictionary = []
        for line_idx, line in enumerate(file):
            if IS_DEBUG:
                print('\n' + str(line_idx) + '.\t' + line)

            engine_schematics = re.findall(
                "(?:\d)+|[?:.]+|[-!$#%^&@*()_+|~=`\{\}\[\]:\";'<>?,\/]", line)
            char_idx = 0

            current_line_engine_schematics_ref = [None] * len(line)
            for engine_schematic in engine_schematics:

                if engine_schematic[0] == '.':
                    char_idx += len(engine_schematic)
                    continue
                if IS_DEBUG:
                    print('\nengine schematic: ' + engine_schematic)

                # create a variable that shares memory between multiple indecies
                # used to prevent double counting an engine if it touches multiple symbols
                engine_schematic_ref = [engine_schematic]

                for i, length in enumerate(engine_schematic):

                    # have each character length of the schematic associated with the reference
                    # this will make doing a search and deletion for the schematic easier after the schematic has been counted
                    current_line_engine_schematics_ref[char_idx +
                                                       i] = engine_schematic_ref

                    # at the engine schematics first char, check back and then diagonally back/forwards
                    if i == 0:

                        # .. but only if we're not at the beginning of the line
                        if char_idx != 0:
                            if IS_DEBUG:
                                print('\tpeek back: ', end='')
                                print(
                                    current_line_engine_schematics_ref[char_idx-1])
                            if IS_PART1:
                                total += get_adjacent_increment(
                                    engine_schematic_ref, current_line_engine_schematics_ref[char_idx-1])
                            else:
                                get_gear_ratio(str(line_idx) + '-' + str(char_idx), engine_schematic_ref, str(
                                    line_idx) + '-' + str(char_idx-1), current_line_engine_schematics_ref[char_idx-1])

                        # .. and we're not at the beginning of the file
                        if line_idx != 0:
                            if IS_DEBUG:
                                print('\tpeek diagonal back: ', end='')
                                print(prev_line_dictionary[char_idx-1])
                            if IS_PART1:
                                total += get_adjacent_increment(
                                    engine_schematic_ref, prev_line_dictionary[char_idx-1])
                            else:
                                get_gear_ratio(str(line_idx) + '-' + str(char_idx), engine_schematic_ref, str(
                                    line_idx-1) + '-' + str(char_idx-1), prev_line_dictionary[char_idx-1])

                    if line_idx != 0:
                        if IS_DEBUG:
                            print('\tpeek above: ', end='')
                            print(prev_line_dictionary[char_idx+i])

                        if IS_PART1:
                            total += get_adjacent_increment(
                                engine_schematic_ref, prev_line_dictionary[char_idx+i])
                        else:
                            get_gear_ratio(str(line_idx) + '-' + str(char_idx), engine_schematic_ref, str(
                                line_idx-1) + '-' + str(char_idx+i), prev_line_dictionary[char_idx+i])

                # after all characters are iterated, do one last diagonal check
                if line_idx != 0:
                    if IS_DEBUG:
                        print('\tpeek diagonal forward: ', end='')
                        print(
                            prev_line_dictionary[char_idx+len(engine_schematic)])

                    if IS_PART1:
                        total += get_adjacent_increment(
                            engine_schematic_ref, prev_line_dictionary[char_idx+len(engine_schematic)])
                    else:
                        get_gear_ratio(str(line_idx) + '-' + str(char_idx),
                                       engine_schematic_ref,
                                       str(line_idx-1) + '-' +
                                       str(char_idx+len(engine_schematic)),
                                       prev_line_dictionary[char_idx+len(engine_schematic)])

                char_idx += len(engine_schematic)

            prev_line_dictionary = current_line_engine_schematics_ref

        if not IS_PART1 and IS_DEBUG:
            print('\nall\n')
            print(gear_ratio)

            print('\nfilter\n')
            print(list(filter(lambda item: len(item[1]) == 2, gear_ratio.items())))

            print('\nmap\n')
            print(list(map(lambda x: int(x[1][0]) * int(x[1][1]),
                                filter(lambda item: len(item[1]) == 2, gear_ratio.items()))))
            

        if IS_PART1:
            print(gear_ratio)
        else:
            print(reduce(lambda x, y: x + y,
                         map(lambda x: int(x[1][0]) * int(x[1][1]),
                             filter(lambda item: len(item[1]) == 2, gear_ratio.items()))))


func()
