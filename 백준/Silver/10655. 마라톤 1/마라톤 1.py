import sys
import math
input = sys.stdin.readline


def init_data():
    total_checkpoints = int(input())
    checkpoints = [list(map(int, input().split()))
                   for _ in range(total_checkpoints)]

    return total_checkpoints, checkpoints


def manhattan_distance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def min_distance(total_checkpoints, checkpoints):

    intervals = [0]+[manhattan_distance(checkpoints[i], checkpoints[i-1])
                     for i in range(1, total_checkpoints)]
    origin_distance = sum(intervals)

    min_dist = math.inf
    for j in range(1, total_checkpoints-1):
        min_dist = min(min_dist, origin_distance -
                       intervals[j] - intervals[j+1]+manhattan_distance(checkpoints[j+1], checkpoints[j-1]))

    return min_dist


if __name__ == '__main__':
    total_checkpoints, checkpoints = init_data()
    print(min_distance(total_checkpoints, checkpoints))
