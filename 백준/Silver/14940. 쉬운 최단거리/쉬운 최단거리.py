import sys
import copy
from collections import deque
input = sys.stdin.readline


def init_data():
    height, width = map(int, input().split())
    boards = []
    target = [0, 0]
    for i in range(height):
        row = list(map(int, input().split()))
        boards.append(row)
        for j in range(width):
            if row[j] == 2:
                target = [i, j]

    return height, width, boards, target


def in_range(pos, height, width):
    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        return True
    return False


def update_distance(target, height, width, boards):
    DIRECTION = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited = [[False]*width for _ in range(height)]
    visited[target[0]][target[1]] = True

    queue = deque([])
    queue.append(target)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+DIRECTION[i][0]
            ny = y+DIRECTION[i][1]
            if in_range([nx, ny], height, width):
                if not visited[nx][ny] and boards[nx][ny] != 0:
                    boards[nx][ny] = boards[x][y] + 1
                    queue.append([nx, ny])
                    visited[nx][ny] = True

    return visited, boards


if __name__ == '__main__':
    height, width, boards, target = init_data()
    distance_map = copy.deepcopy(boards)

    distance_map[target[0]][target[1]] = 0
    visited, distance_map = update_distance(
        target, height, width, distance_map)

    for i in range(height):
        for j in range(width):
            if distance_map[i][j] == 1 and visited[i][j] == False:
                print(-1, end=" ")
            else:
                print(distance_map[i][j], end=" ")
        print()
