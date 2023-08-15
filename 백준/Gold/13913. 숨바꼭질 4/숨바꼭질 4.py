import sys
from collections import deque
input = sys.stdin.readline


def init_data():
    start, end = map(int, input().split())
    return start, end


def find_min_time(start, end):
    visited = [0]*(100001)
    path = [0]*(100001)

    if start == end:
        path[start] = end
        return path, 0

    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for nxt in [cur-1, cur+1, 2*cur]:
            if nxt > 100000 or nxt < 0:
                continue
            if visited[nxt] == 0:
                visited[nxt] += visited[cur]+1
                path[nxt] = cur
                queue.append(nxt)
                if nxt == end:
                    return path, visited[end]

    return "Fail to arrive"


def find_route(path, start, end):
    cur = end
    route = [end]
    while cur != start:
        route.append(path[cur])
        cur = path[cur]
    return route[::-1]


if __name__ == '__main__':
    start, end = init_data()
    path, dist = find_min_time(start, end)
    print(dist)
    print(*find_route(path, start, end), end="")
