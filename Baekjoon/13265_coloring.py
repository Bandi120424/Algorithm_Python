import sys
from collections import deque
input = sys.stdin.readline


def circle_coloring(queue):

    while queue:
        cur_vertex = queue.popleft()
        for connected_vertex in graph[cur_vertex]:
            if painted_colors[connected_vertex] != 0:
                if painted_colors[connected_vertex] == painted_colors[cur_vertex]:
                    return False
            if not painted_colors[connected_vertex]:
                painted_colors[connected_vertex] = painted_colors[cur_vertex] * \
                    (-1)
                queue.append(connected_vertex)

    return True


# def init_data():
num_of_cases = int(input())
for i in range(num_of_cases):
    num_of_vertexes, num_of_edges = map(int, input().split())
    graph = [[] for _ in range(num_of_vertexes+1)]

    for _ in range(num_of_edges):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    painted_colors = [0] * (num_of_vertexes+1)
    option = "possible"

    for vertex in range(1, num_of_vertexes+1):
        if not painted_colors[vertex]:
            painted_colors[vertex] = 1
            queue = deque()
            queue.append(vertex)
            if not circle_coloring(queue):
                option = "impossible"
                break
    print(option)
