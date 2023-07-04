import sys
from collections import deque
input = sys.stdin.readline


def init_data():
    total_number = int(input())
    seq = [int(input()) for _ in range(total_number)]
    return total_number, seq[::-1]


def make_seq(total_number, seq):
    stack = []
    ops = []

    for idx in range(1, total_number+1):
        stack.append(idx)
        ops.append('+')

        while seq and stack:
            if seq[-1] == stack[-1]:
                seq.pop()
                stack.pop()
                ops.append('-')
            else:
                break

    return ops if len(seq) == 0 else ["NO"]


if __name__ == '__main__':
    total_number, seq = init_data()
    for op in make_seq(total_number, seq):
        print(op)
