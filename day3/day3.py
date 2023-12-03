import re

IS_PART1 = False
IS_DEBUG = False


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

                            total += get_adjacent_increment(
                                engine_schematic_ref, current_line_engine_schematics_ref[char_idx-1])

                        # .. and we're not at the beginning of the file
                        if line_idx != 0:
                            if IS_DEBUG:
                                print('\tpeek diagonal back: ', end='')
                                print(prev_line_dictionary[char_idx-1])

                            total += get_adjacent_increment(
                                engine_schematic_ref, prev_line_dictionary[char_idx-1])

                    if line_idx != 0:
                        if IS_DEBUG:
                            print('\tpeek above: ', end='')
                            print(prev_line_dictionary[char_idx+i])

                        total += get_adjacent_increment(
                            engine_schematic_ref, prev_line_dictionary[char_idx+i])

                # after all characters are iterated, do one last diagonal check
                if line_idx != 0:
                    if IS_DEBUG:
                        print('\tpeek diagonal forward: ', end='')
                        print(
                            prev_line_dictionary[char_idx+len(engine_schematic)])

                    total += get_adjacent_increment(
                        engine_schematic_ref, prev_line_dictionary[char_idx+len(engine_schematic)])

                char_idx += len(engine_schematic)

            prev_line_dictionary = current_line_engine_schematics_ref

        print(total)


func()
