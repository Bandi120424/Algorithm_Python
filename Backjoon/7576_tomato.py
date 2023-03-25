import sys
from collections import deque
input = sys.stdin.readline

def init():
    """입력 처리 

    Returns:
        list: 초기 토마토 현황 
    """
    width, height = map(int, input().split())
    tomatoes = [list(map(int, input().split())) for _ in range(height)]

    return tomatoes


def find_initial_pos(tomatoes: list,  width: int = 0, height: int = 0):
    """초기 토마토들의 위치를 반환 
    Args:
        tomatoes (list, optional): 토마토 상자 현황
        width (int, optional): 토마토 상자 너비. Defaults to 0.
        height (int, optional): 토마토 상자 높이. Defaults to 0.

    Returns:
        tomato_pos: 초기 토마토들의 위치를 담은 배열 
    """
    initial_pos = deque([])

    for i in range(height):
        for j in range(width):
            if tomatoes[i][j] == 1:
                initial_pos.append([i, j])

    return initial_pos


def in_range(pos: list = [0, 0], width: int = 0, height: int = 0):
    """체크할 위치가 유효한지를 확인 

    Args:
        pos (list, optional): 체크할 위치. Defaults to [0, 0].
        width (int, optional): 토마토 상자 너비. Defaults to 0.
        height (int, optional): 토마토 상자 높이. Defaults to 0.

    Returns:
        boolean: 토마토 위치의 유효여부
    """
    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        return True
    return False


def ripen(tomatoes: list, initial_pos: deque, width: int = 0, height: int = 0):
    """토마토들의 상태 업데이트 
       익은 토마토들을 기준으로 bfs를 수행하여 주변의 토마토들을 성숙시킴
       bfs의 최댓값이 최대로 많은 토마토들을 성숙시킬 수 있는 기간임 

    Args:
        tomatoes (list): 토마토 상자 
        initial_pos (deque): 익은 토마토들의 초기 위치 
        width (int, optional): 토마토 상자 너비. Defaults to 0.
        height (int, optional): 토마토 상자 높이. Defaults to 0.


    Returns:
        tomatoes: 최대 기간으로 성숙과정을 거친 토마토 상자 
    """
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while initial_pos:
        x, y = initial_pos.popleft()
        # 익은 토마토들의 상하좌우를 살피며 익지 않은 상태의 토마토들을 익게만듦
        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]
            if in_range([nx, ny], width, height) and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                initial_pos.append([nx, ny])
    return tomatoes


def unripened_check(tomatoes: list):
    """토마토 상자에 익지 않은 토마토가 있는지 확인 

    Args:
        tomatoes (list): 토마토 현황

    Returns:
        int: 토마토 상자의 모든 토마토를 성숙시키는 데 걸리는 기간 
    """
    max_days = 0
    for row in tomatoes:
        max_days = max(max_days, max(row))
        for i in row:
            if i == 0:  # 익히지 못한 토마토가 있는 경우
                return -1
    return max_days - 1


def run():
    tomatoes = init()
    width = len(tomatoes[0])
    height = len(tomatoes)

    initial_pos = find_initial_pos(tomatoes, width, height)
    new_tomatoes = ripen(tomatoes, initial_pos, width, height)

    ans = unripened_check(new_tomatoes)
    print(ans)


# execute
run()
