import re

IS_PART1 = False
IS_DEBUG = False


def func():
    total = 0
    report = []
    with open('./day9/actual-input.txt', 'r', encoding="utf8") as file:

        pattern = re.compile(r'-?[\w]+')

        for idx, line in enumerate(file):
            report.append([int(x) for x in re.findall(pattern, line)])

    revised_report = []

    for history in report:

        # Start the sequence of difference with the actual historical recording
        sequence_of_differences = [history]

        is_zero = False

        # Go through each sequence of differences until a row of zeros is found
        while not is_zero:

            next_sequence = None
            # For each value in the sequence of differences
            for idx, value in enumerate(sequence_of_differences[-1]):

                # Create the next sequence of differences
                if idx == 0:
                    next_sequence = []

                # Compare the current value against the previous
                #   and append the result to the next sequence
                else:
                    previous_value = sequence_of_differences[-1][idx-1]
                    next_sequence.append(value-previous_value)

            sequence_of_differences.append(next_sequence)

            if all(x == 0 for x in next_sequence):
                is_zero = True

        revised_report.append(sequence_of_differences)

    for idx, history in enumerate(revised_report):

        if IS_DEBUG:
            print('\nStarting history for: ', end='')
            print(history)

        sequence_of_difference = history.pop()
        increment = 0
        while len(history) >= 0:
            val = sequence_of_difference.pop() if IS_PART1 else sequence_of_difference.pop(0)
            if IS_DEBUG:
                print('  Add ' + str(val) + ' to ' +
                      str(increment) + ' for a total of ', end='')
            increment = val + (increment if IS_PART1 else -increment)

            if IS_DEBUG:
                print(str(increment) + '.')

            if len(history) != 0:
                sequence_of_difference = history.pop()
            else:
                break
        if IS_DEBUG:
            print(str(increment) + ' captured for this sequence of differences.')
        total += increment

    if IS_DEBUG:
        print('\nFinal sum is: ', end='')
    print(total)


func()
