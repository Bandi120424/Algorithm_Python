import sys
from collections import deque
input = sys.stdin.readline
# https://www.acmicpc.net/problem/2206


def init_data():
    height, width = map(int, input().split())
    board = [[int(x) for x in input().strip()] for _ in range(height)]

    return height, width, board


def in_range(pos, width, height):
    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        return True
    return False


def find_wayout(pos, break_wall, board, width, height):
    queue = deque()
    y, x = pos
    queue.append([y, x, break_wall])
    DXS = [0, 0, 1, -1]
    DYS = [1, -1, 0, 0]
    visited = [[[0]*2 for _ in range(width)]
               for _ in range(height)]  # 3차원배열 안쓸 수 없나
    visited[0][0][0] = 1

    while queue:
        y, x, break_wall = queue.popleft()

        if y == (height - 1) and x == (width - 1):
            return visited[y][x][break_wall]

        for i in range(4):
            ny = y + DYS[i]
            nx = x + DXS[i]
            if in_range([ny, nx], width, height):
                if board[ny][nx] == 0 and visited[ny][nx][break_wall] == 0:  # 이동가능하면서 아직 방문하지 않은 곳
                    visited[ny][nx][break_wall] = visited[y][x][break_wall]+1
                    queue.append([ny, nx, break_wall])
                if board[ny][nx] == 1 and break_wall == 0:  # 벽 파괴 사용
                    # break_wall = 1
                    visited[ny][nx][1] = visited[y][x][0]+1
                    queue.append([ny, nx, 1])

    return -1


if __name__ == '__main__':
    height, width, board = init_data()
    break_wall = 0
    print(find_wayout([0, 0], break_wall, board, width, height))
