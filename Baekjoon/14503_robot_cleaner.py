import sys
input = sys.stdin.readline

# input data parsing
def init_data():
    height, width = map(int, input().split())
    x, y, direction = map(int, input().split())
    initial_info = [x, y, direction]
    room_map = [list(map(int, input().split())) for _ in range(height)]
    room_map[x][y] = 2  # 청소가 완료된 방의 값은 2로 변경
    return [initial_info, room_map]


def in_range(pos: list = [0, 0], width: int = 0, height: int = 0):
    """체크할 위치가 유효한지를 확인
    Args:
        pos (list, optional): 체크할 위치. Defaults to [0, 0].
        width (int, optional): 방 너비. Defaults to 0.
        height (int, optional): 방 높이. Defaults to 0.

    Returns:
        boolean: 현 위치의 유효여부
    """
    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        return True
    return False


def clean_room(robot_info: list, room_map: list):
    """주변을 탐색하며 청소 

    Args:
        robot_info (list): 로봇의 현 위치, 방향 정보 
        room_map (list): 방 청소 상태 

    Returns:
        int : 청소된 방의 수 
    """
    x, y, direction = robot_info
    width, height = len(room_map[0]), len(room_map)
    # exit_flag = False
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    cleaned_room_cnt = 1

    while True:
        near_clean = False
        for _ in range(4):
            direction = (direction+3) % 4
            nx = x + dxs[direction]
            ny = y + dys[direction]

            if in_range([nx, ny], width, height) and room_map[nx][ny] == 0:
                room_map[nx][ny] = 2
                cleaned_room_cnt += 1
                x, y = nx, ny
                near_clean = True
                break

        if not near_clean:  # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            if room_map[x-dxs[direction]][y-dys[direction]] == 1:
                break
            else:
                x, y = x-dxs[direction], y-dys[direction]
    return cleaned_room_cnt


def run():
    initial_info, room_map = init_data()
    cleaned_room_ctn = clean_room(initial_info, room_map)

    print(cleaned_room_ctn)


run()
