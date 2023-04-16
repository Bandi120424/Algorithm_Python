import sys
from collections import deque
input = sys.stdin.readline

def in_range(pos, width, height):
    if (0 <= pos[0] < height) and (0 <= pos[1] < width):
        return True
    return False
    
def find_island(start, width, height): #maps 일단 global 변수로 
    queue = deque()
    queue.append(start)
    DXS = [-1, 1, 0, 0, -1, -1, 1, 1]
    DYS = [0, 0, -1, 1, -1, 1, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + DXS[i]
            ny = y + DYS[i]
            if in_range([nx, ny], width, height) and (maps[nx][ny] == 1):
                maps[nx][ny] += 1
                queue.append([nx, ny])
                find_island([nx, ny], width, height)

island_list = []
while True:
    
    width, height = map(int, input().split())
    if (width == 0) and (height == 0):
        break  
        
    maps = [[int(x) for x in input().split()] for _ in range(height)]

    island_cnt = 0
    for x in range(height):
        for y in range(width):
            if (maps[x][y] == 1):
                maps[x][y] += 1
                island_cnt += 1
                find_island([x, y], width, height)
    
    island_list.append(island_cnt)
    
for num in island_list:
    print(num)
