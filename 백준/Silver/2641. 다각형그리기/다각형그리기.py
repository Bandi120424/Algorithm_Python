import sys
input = sys.stdin.readline

sequence_len = int(input())
sample_sequence = ''.join(input().split())
num_of_sequences = int(input())
sequences = [''.join(input().split()) for _ in range(num_of_sequences)]

# method 1


def opposite_direction(direction: int = 0):

    if direction % 2 == 1:
        return (direction+2) % 4

    # if direction % 2 == 0:
    if direction == 2:
        return 4

    if direction == 4:
        return 2


def opposite_sequence(sequence=None):

    if sequence == None:
        return ""

    seq2int = list(map(int, sequence[::-1]))
    opposite_seq = ""
    for num in seq2int:
        opposite_seq += str(opposite_direction(num))

    return opposite_seq


def possible_cases(sequence=None):

    if sequence == None:
        return list()

    all_cases = [sequence]

    for i in range(len(sequence)):
        all_cases.append(sequence[i:]+sequence[:i])

    return all_cases


def find_match(cases=None, sequences=None):

    if cases == None or sequences == None:
        return list()

    matched_list = []
    for c in sequences:
        if c in cases:
            matched_list.append(c)

    return matched_list


def solution():
    all_cases = possible_cases(sample_sequence) + \
        possible_cases(opposite_sequence(sample_sequence))
    matched_list = find_match(all_cases, sequences)

    print(len(matched_list))
    for seq in matched_list:
        for i in range(sequence_len):
            if i == sequence_len - 1:
                print(seq[i])
            else:
                print(seq[i], end=" ")


solution()