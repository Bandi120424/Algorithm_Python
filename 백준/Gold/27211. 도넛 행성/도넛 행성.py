import sys
from collections import deque
input = sys.stdin.readline

height, width = map(int, input().split())
planet_map = [list(map(int, input().split())) for _ in range(height)]


def search_area(start):
    queue = deque([])
    queue.append(start)
    DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    while queue:
        y, x = queue.popleft()
        for dy, dx in DIRECTIONS:
            ny = (y+dy) % height
            nx = (x+dx) % width
            if (planet_map[ny][nx] == 0):
                planet_map[ny][nx] += 1
                queue.append([ny, nx])


area_cnt = 0
for i in range(height):
    for j in range(width):
        if planet_map[i][j] == 0:
            planet_map[i][j] += 1
            area_cnt += 1
            search_area([i, j])

print(area_cnt)
