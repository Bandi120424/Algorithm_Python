import sys
from collections import deque
input = sys.stdin.readline


def init_data():
    total_companies, total_relation = map(int, input().split())
    given_relation = [[] for _ in range(total_companies+1)]
    for _ in range(total_relation):
        v1, v2 = map(int, input().split())
        given_relation[v2].append(v1)  # v2 then v1

    return total_companies, given_relation


def make_connection(start, total_companies, given_relation):
    queue = deque()
    queue.append(start)
    connection = 1
    visited = [False]*(total_companies+1)
    visited[start] = True
    while queue:
        pos = queue.popleft()
        for next_pos in given_relation[pos]:
            if visited[next_pos] == False:
                connection += 1
                queue.append(next_pos)
                visited[next_pos] = True

    return connection


if __name__ == "__main__":
    total_companies, given_relation = init_data()
    connections = [0]+[make_connection(idx, total_companies, given_relation)
                       for idx in range(1, total_companies+1)]
    for idx in range(1, total_companies+1):
        if connections[idx] == max(connections):
            print(idx, end=' ')