import sys
from collections import defaultdict
input = sys.stdin.readline


def init_data():
    total_stuff = int(input())
    total_pairs = int(input())
    comparison_graph = [[False]*total_stuff for _ in range(total_stuff)]
    for _ in range(total_pairs):
        a, b = map(int, input().split())
        comparison_graph[a-1][b-1] = True

    return total_stuff, comparison_graph


def connection(total_stuff, comparison_graph):
    for k in range(total_stuff):
        for i in range(total_stuff):
            for j in range(total_stuff):
                if comparison_graph[i][k] and comparison_graph[k][j]:
                    comparison_graph[i][j] = True

    return comparison_graph


if __name__ == '__main__':
    total_stuff, comparison_graph = init_data()
    graph = connection(total_stuff, comparison_graph)
    for i in range(total_stuff):
        cnt = 0
        for j in range(total_stuff):
            if not graph[i][j] and not graph[j][i]:
                cnt += 1
        print(cnt-1)
