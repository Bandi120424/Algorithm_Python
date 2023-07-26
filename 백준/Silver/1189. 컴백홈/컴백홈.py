import sys
input = sys.stdin.readline


def in_range(pos):
    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        return True
    else:
        return False


def dfs(x, y, cnt):
    global ans

    if [x, y] == [0, width-1]:
        if cnt == distance:
            ans += 1
            return

    DXS = [-1, 1, 0, 0]
    DYS = [0, 0, -1, 1]
    for i in range(4):
        nx = x + DXS[i]
        ny = y + DYS[i]
        if in_range([nx, ny]) and board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = False


# 입력값 처리
height, width, distance = map(int, input().split())
board = [list(1 if item == '.' else 0 for item in input().strip())
         for _ in range(height)]
visited = [[False]*width for _ in range(height)]
ans = 0

visited[height-1][0] = True
dfs(height-1, 0, 1)
print(ans)
