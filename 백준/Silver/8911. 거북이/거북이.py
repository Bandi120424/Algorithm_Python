import sys
input = sys.stdin.readline


def init_data():
    cases_num = int(input())
    total_cases = [input() for _ in range(cases_num)]
    return total_cases


def move(pos, cur_dir, order):
    DXS, DYS = [0, 1, 0, -1], [1, 0, -1, 0]  # direction = N:0, E:1, S:2, W:3
    x, y = pos[0], pos[1]
    if order == 'F':
        return [x+DXS[cur_dir], y+DYS[cur_dir]]
    else:  # order == 'B'
        return [x+DXS[(cur_dir+2) % 4], y+DYS[(cur_dir+2) % 4]]


def change_dir(cur_dir, order):
    if order == 'L':
        return (cur_dir - 1) % 4
    else:  # order == 'R'
        return (cur_dir + 1) % 4


def find_area(orders):
    path = [[0, 0]]
    dir = 0
    for odr in orders:
        if odr in {'F', 'B'}:
            path.append(move(path[-1], dir, odr))
        if odr in {'L', 'R'}:
            dir = change_dir(dir, odr)

    path_x = [i[0] for i in path]
    path_y = [i[1] for i in path]

    width = max(path_x) - min(path_x)
    height = max(path_y) - min(path_y)

    return width*height


if __name__ == '__main__':
    total_cases = init_data()
    for case in total_cases:
        print(find_area(case))
