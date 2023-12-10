import re

IS_DEBUG = False

SORT_ORDER = {"A": 14, "K": 13, "Q": 12, "J": 0, "T": 10, "9": 9, "8": 8,
              "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1}

TYPE = {"Five of a kind": 6,
        "Four of a kind": 5,
        "Full house": 4,
        "Three of a kind": 3,
        "Two pair": 2,
        "One pair": 1,
        "High card": 0}

X_OF_A_KIND_TO_TYPE = {
    5: TYPE["Five of a kind"],
    4: TYPE["Four of a kind"],
    3: TYPE["Three of a kind"],
    2: TYPE["One pair"]
}


def func():

    hands = []
    with open('./day7/actual-input.txt', 'r', encoding="utf8") as file:

        for line in file:

            hand = {}
            [cards_unsorted, bid] = line.split(" ")
            cards_sorted = sorted(list(cards_unsorted),
                                  key=lambda val: (-1 * SORT_ORDER[val]))

            cards = ''.join(map(str, cards_sorted))

            hand['cards'] = cards
            hand['unsorted'] = cards_unsorted

            pattern = re.compile(r'([A-I]|[K-Z]|[2-9])\1+')

            candidate_types = []

            for itr in re.finditer(pattern, cards):
                candidate_types.append(len(itr.group()))

            jokers = 0
            pattern_jokers = re.compile(r'[jJ]+')
            for itr in re.finditer(pattern_jokers, cards):
                jokers += len(itr.group())

            # It appears that the wildcard will increment the hand type 'up' by one tier
            if jokers != 0:
                if len(candidate_types) == 0:

                    # Unique path for when the hand is all jokers.
                    if jokers == 5:
                        candidate_types.append(jokers)
                    
                    # Or for when it's just a type of High Cards
                    else:
                        candidate_types.append(jokers + 1)

                elif len(candidate_types) == 1:
                    candidate_types[0] += jokers
                elif len(candidate_types) == 2:

                    # Unique path to identify if a Full House or Two Pair
                    if candidate_types[0] == 3:
                        candidate_types[0] += jokers
                    elif candidate_types[1] == 3:
                        candidate_types[1] += jokers
                    else:
                        candidate_types[0] += jokers

            # if there are more than one same same cards in the hand
            if len(candidate_types) == 1:
                hand['type'] = X_OF_A_KIND_TO_TYPE[candidate_types[0]]
            elif len(candidate_types) == 2:
                if (candidate_types[0] == 3 or candidate_types[1] == 3):
                    hand['type'] = TYPE["Full house"]
                else:
                    hand['type'] = TYPE["Two pair"]
            else:
                hand['type'] = TYPE["High card"]

            hand['bid'] = int(bid)

            hand['card_unsorted'] = list(
                map(lambda x: SORT_ORDER[x], cards_unsorted))

            hand['cards_sorted'] = list(
                map(lambda x: SORT_ORDER[x], cards_sorted))

            hands.append(hand)

    hands_sorted = sorted(list(hands), key=lambda val: (
        val['type'], val['card_unsorted']), reverse=True)

    calculation = []
    for idx, hand in enumerate(hands_sorted):
        hand.update({'weight': (len(hands_sorted) - idx)})
        calculation.append(hand)

    if IS_DEBUG:
        print(*calculation, sep='\n')

    total = 0
    for calc in calculation:
        total += calc['weight'] * calc['bid']

    print(total)


func()
