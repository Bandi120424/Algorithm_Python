import sys
from collections import defaultdict
input = sys.stdin.readline
# https://www.acmicpc.net/problem/1034


def init_data():
    height, width = map(int, input().split())
    ramps = [input().strip() for _ in range(height)]
    switch = int(input())
    return height, width, ramps, switch

def to_turnon(ramps, switch):
    turn_on = defaultdict(int)
    for row in ramps:
        offctn = row.count('0')
        if offctn <= switch and offctn%2 == switch%2:
            turn_on[row] += 1
    return turn_on

if __name__ == '__main__':
    height, width, ramps, switch = init_data()
    turn_on = to_turnon(ramps, switch)
    if len(turn_on) == 0:
        print(0)
        exit()
        
    turn_on_sort = sorted(turn_on.items(), key=lambda x:x[1])
    print(turn_on_sort[-1][1])
        



