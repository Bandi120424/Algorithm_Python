import sys
from itertools import permutations
input = sys.stdin.readline


def init_data():
    total_numbers = int(input())
    numbers = list(map(int, input().split()))

    return total_numbers, numbers


def sum_diff(orders, total_numbers, numbers):
    s_value = 0
    for i in range(total_numbers-1):
        s_value += abs(numbers[orders[i]]-numbers[orders[i+1]])
    return s_value


def find_maxdiff(total_numbers, numbers):
    whole_cases = permutations(
        [i for i in range(total_numbers)], total_numbers)
    max_val = 0
    for case in whole_cases:
        max_val = max(max_val, sum_diff(case, total_numbers, numbers))

    return max_val


if __name__ == "__main__":
    total_numbers, numbers = init_data()
    print(find_maxdiff(total_numbers, numbers))
