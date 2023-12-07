import re
from functools import reduce

IS_PART1 = False
IS_DEBUG = False


def func():

    card_winner_counts = []

    total = 0
    with open('./day4/actual-input.txt', 'r', encoding="utf8") as file:
        for line_idx, line in enumerate(file):
            [card, numbers] = line.split(': ')
            [winning_numbers_str, actual_numbers_str] = numbers.split(' | ')
            winning_numbers = [int(x) for x in re.findall('[\d]+', winning_numbers_str)]
            actual_numbers = [int(x) for x in re.findall('[\d]+', actual_numbers_str)]

            count = 0
            for actual_number in actual_numbers:
                if actual_number in winning_numbers:
                    count += 1

            if IS_PART1:

                increment = 1 if count == 1 else pow(2, count-1) if count > 1 else 0

                if IS_DEBUG:
                    print('\n'+line.strip())
                    print('Count: ' + str(increment))

                total += increment

            else:
                card_winner_counts.append(count)

    if not IS_PART1:
        total_scratch_cards = [1] * len(card_winner_counts)

        for i, card_winner_count in enumerate(card_winner_counts):
            for _ in range(total_scratch_cards[i]):
                for k in range(card_winner_count):
                    total_scratch_cards[i + 1 + k] += 1

        total = reduce(lambda x, y: x + y, total_scratch_cards, 0)

    print(total)


func()
