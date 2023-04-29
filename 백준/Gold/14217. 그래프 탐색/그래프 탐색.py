# https://www.acmicpc.net/problem/14217
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def init_data():
    num_of_cities, num_of_roads = map(int, input().split())

    roads_graph = defaultdict(list)
    for _ in range(num_of_roads):
        v1, v2 = map(int, input().split())
        roads_graph[v1].append(v2)
        roads_graph[v2].append(v1)

    repair_roads_num = int(input())
    repair_plans = [list(map(int, input().split()))
                    for _ in range(repair_roads_num)]
    return num_of_cities, roads_graph, repair_plans

def repair_roads(repair_plan):  # roads_graph: global
    opt, v1, v2 = repair_plan
    global roads_graph
    if opt == 1:
        roads_graph[v1].append(v2)
        roads_graph[v2].append(v1)
    if opt == 2:
        roads_graph[v1].remove(v2)
        roads_graph[v2].remove(v1)
    return roads_graph

def visit_ctn(roads_graph, num_of_cities):
    visited = [-1]*(num_of_cities+1)
    visited[1] = 0
    queue = deque()
    queue.append(1)
    while queue:
        cur_pos = queue.popleft()
        for city in roads_graph[cur_pos]:
            if visited[city] == -1:
                visited[city] = visited[cur_pos] + 1
                queue.append(city)
    return visited[1:]

if __name__ == "__main__":
    num_of_cities, roads_graph, repair_plans = init_data()
    for plan in repair_plans:
        print(*visit_ctn(repair_roads(plan), num_of_cities))