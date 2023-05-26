import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict
input = sys.stdin.readline


def init_data():
    clover_num, total_orders = map(int, input().split())
    clover_x, clover_y = defaultdict(list), defaultdict(list)
    for _ in range(clover_num):
        x, y = map(int, input().split())
        clover_x[x].append(y)
        clover_y[y].append(x)

    for key, value in clover_x.items():
        clover_x[key] = sorted(value)
    for key, value in clover_y.items():
        clover_y[key] = sorted(value)

    orders = [x for x in input().strip()]

    return clover_x, clover_y, orders


def find_clover(clover_x, clover_y, pos, order):
    x, y = pos
    if order == 'L':
        x = clover_y[y][bisect_left(clover_y[y], x)-1]
    if order == 'R':
        x = clover_y[y][bisect_right(clover_y[y], x)]
    if order == 'U':
        y = clover_x[x][bisect_right(clover_x[x], y)]
    if order == 'D':
        y = clover_x[x][bisect_left(clover_x[x], y)-1]

    return x, y


if __name__ == '__main__':
    clover_x, clover_y, orders = init_data()
    x, y = 0, 0
    for order in orders:
        x, y = find_clover(clover_x, clover_y, [x, y], order)

    print(x, y)
