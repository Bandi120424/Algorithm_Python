import sys
import copy
from itertools import combinations
input = sys.stdin.readline

class Lab():
    def __init__(self, height: int = 0, width: int = 0, lab_map=None) -> None:
        self.height = height
        self.width = width
        self.lab_map = lab_map

    def find_virusNempty(self):
        if self.lab_map == None:
            raise Exception("in class Lab: Lab map is None")

        virus_pos, empty_pos = [], []
        for i in range(self.height):
            for j in range(self.width):
                if self.lab_map[i][j] == 2:
                    virus_pos.append([i, j])
                if self.lab_map[i][j] == 0:
                    empty_pos.append([i, j])
        return virus_pos, empty_pos


def init_data():
    height, width = map(int, input().split())
    lab_map = [list(map(int, input().split())) for _ in range(height)]
    return Lab(height, width, lab_map)


def in_range(pos, height: int = 0, width: int = 0):
    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        return True
    return False


def build_wall(lab_map=None, pos=None):

    if lab_map == None:
        raise Exception("in func build_wall: lab_map is None")
    if pos == None:
        raise Exception("in func build_wall: pos is None")

    new_lab_map = copy.deepcopy(lab_map)
    for p in pos:
        new_lab_map[p[0]][p[1]] = 1
    return new_lab_map


def spread_virus(height: int = 0, width: int = 0, lab_map=None, virus=None):

    if lab_map == None:
        raise Exception("in spread_virus, lab_map is None")
    if virus == None:
        raise Exception("in spread_virus, virus is None")

    DIRECTION = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while virus:
        x, y = virus.pop()
        for dx, dy in DIRECTION:
            nx = x + dx
            ny = y + dy
            if in_range([nx, ny], height, width) and lab_map[nx][ny] == 0:
                lab_map[nx][ny] = 2
                virus.append([nx, ny])
    return lab_map


def count_safezone(lab_map=None):
    if lab_map == None:
        raise Exception("in search_safezone, lab_map is None")

    cnt = 0
    for row in lab_map:
        cnt += row.count(0)
    return cnt


def find_max_safezone(lab_info, num_of_walls):
    virus_pos, empty_pos = lab_info.find_virusNempty()

    if len(empty_pos) < num_of_walls:
        raise Exception("Impossible to build walls")

    max_safezone = 0
    whole_cases = combinations(empty_pos, num_of_walls)
    for case in whole_cases:
        new_lab_map = build_wall(copy.deepcopy(lab_info.lab_map), case)
        updated_map = spread_virus(
            lab_info.height, lab_info.width, new_lab_map, copy.deepcopy(virus_pos))
        max_safezone = max(max_safezone, count_safezone(updated_map))

    return max_safezone


if __name__ == "__main__":
    lab_info = init_data()
    print(find_max_safezone(lab_info, 3))
