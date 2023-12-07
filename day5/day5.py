import re

IS_PART1 = False
IS_DEBUG = False


def func():

    total = 0
    seeds = None
    almanac = []
    last_line_mappings = None
    with open('./day5/actual-input.txt', 'r', encoding="utf8") as file:

        mappings = last_line_mappings = None

        for line_idx, line in enumerate(file):

            if line_idx == 0:
                seeds = [int(x) for x in re.findall('[\d]+', line)]

            elif len(line.strip()) == 0:
                if mappings is not None:
                    almanac.insert(len(almanac), mappings)

            elif ':' in line.strip():
                mappings = last_line_mappings = []

            else:
                mapping = [int(x) for x in re.findall('[\d]+', line)]
                mappings.append(mapping)

    almanac.insert(len(almanac), last_line_mappings)

    for i, mappings in enumerate(almanac):
        print(i)
        temp_mapping = {}

        for j, mapping in enumerate(mappings):
            [destination, source, range_length] = mapping

            for k in range(range_length):
                temp_mapping[source + k] = destination + k
        for idx, seed in enumerate(seeds):
            value = temp_mapping[seed] if seed in temp_mapping else seed
            seeds[idx] = value

    print(min(seeds))


func()
