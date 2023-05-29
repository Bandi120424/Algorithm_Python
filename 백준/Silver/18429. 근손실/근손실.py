import sys
from itertools import permutations
input = sys.stdin.readline


def init_data():
    total_days, weight_loss = map(int, input().split())
    muscle_kit = list(map(int, input().split()))

    return total_days, weight_loss, muscle_kit


def kit(kit, weight_loss):
    weight = 0
    for day in kit:
        weight += (day-weight_loss)
        if weight < 0:
            return False
    return True


def search(muscle_kit, weight_loss):
    all_cases = permutations(muscle_kit)
    case_ctn = 0
    for case in all_cases:
        if kit(case, weight_loss):
            case_ctn += 1
    return case_ctn


if __name__ == '__main__':
    total_days, weight_loss, muscle_kit = init_data()
    print(search(muscle_kit, weight_loss))
