import sys
from collections import defaultdict
input = sys.stdin.readline


def init_data():
    total_numbers = int(input())
    numbers = list(map(int, input().split()))
    max_ctn = int(input())

    return numbers, max_ctn


def make_num(numbers, prev_case, num_list):
    new_case = set([])
    for num in prev_case:
        for given_num in numbers:
            val = num+given_num
            if not num_list[val]:
                num_list[val] = True
                new_case.add(val)
    return list(new_case), num_list


def compute_cases(numbers, max_ctn, num_list):
    cases = defaultdict(list)
    cases[0] = [0]
    num_list[0] = True
    for i in range(1, max_ctn+1):
        cases[i], num_list = make_num(numbers, cases[i-1], num_list)
    return num_list


def find_winner(numbers, max_ctn):
    num_list = [False] * (numbers[-1]*max_ctn+1)  # 정렬된 상태로 숫자가 들어온다고 했음
    loser = compute_cases(numbers, max_ctn, num_list).index(False)
    if loser % 2 == 0:
        print(f"holsoon win at {loser}")
    else:
        print(f"jjaksoon win at {loser}")


if __name__ == '__main__':
    numbers, max_ctn = init_data()
    find_winner(numbers, max_ctn)
