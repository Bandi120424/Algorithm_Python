import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline


def init_data():
    return list(map(int, input().split()))


def find_clock_num(numbers=None):  # numbers는 정수형 리스트
    if numbers == None:
        return ValueError

    value = int(''.join(map(str, numbers)))
    for i in range(1, 4):
        value = min(value, int(''.join(map(str, numbers[i:]+numbers[:i]))))

    return value


def numbertolist(target):
    numbers = []
    remainder = target
    for i in range(3, 0, -1):
        numbers.append(remainder//10**i)
        remainder = remainder % 10**i
    numbers.append(remainder)
    return numbers


def find_order(target):
    start = 1111
    cnt = 0
    # print("target", target)
    while (start <= target):
        start_list = numbertolist(start)
        if 0 not in start_list and find_clock_num(start_list) == start:
            cnt += 1
        start += 1
    return cnt


if __name__ == '__main__':
    numbers = init_data()
    #print(find_clock_num(numbers))
    print(find_order(find_clock_num(numbers)))
