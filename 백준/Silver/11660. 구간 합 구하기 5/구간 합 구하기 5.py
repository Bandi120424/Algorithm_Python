import sys
import copy
input = sys.stdin.readline


def init_data():
    width, total_cases = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(width)]
    cases = [list(map(int, input().split())) for _ in range(total_cases)]

    return width, graph, cases


def compute_sum(graph, width):
    arr_sum = [[0]*(width+1) for _ in range(width+1)]

    for i in range(1, width+1):
        for j in range(1, width+1):
            arr_sum[i][j] = arr_sum[i][j-1] + \
                arr_sum[i-1][j] - arr_sum[i-1][j-1] + graph[i-1][j-1]

    return arr_sum


def partial_sum(graph_sum, case):
    x1, y1, x2, y2 = case
    p_sum = graph_sum[x2][y2] - graph_sum[x2][y1-1] - \
        graph_sum[x1-1][y2] + graph_sum[x1-1][y1-1]
    return p_sum


if __name__ == '__main__':
    width, graph, total_cases = init_data()
    graph_sum = compute_sum(graph, width)
    for case in total_cases:
        print(partial_sum(graph_sum, case))
