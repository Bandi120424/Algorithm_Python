import sys
import copy
input = sys.stdin.readline


class earth():
    def __init__(self, height: int = 0, width: int = 0, earth_map=[]) -> None:
        self.height = height
        self.width = width
        self.earth_map = earth_map
        # 사방에 바다를 두르기
        # self.earth_map = [['.']*self.width]
        # for row in earth_map:
        #     self.earth_map.append(['.']+row+['.'])
        # self.earth_map.append(['.']*self.width)

    def find_land(self) -> list:
        lands = []
        for i in range(self.height):
            for j in range(self.width):
                if self.earth_map[i][j] == 'X':
                    lands.append([i, j])
        return lands

    def in_range(self, pos) -> bool:
        if 0 <= pos[0] < self.height and 0 <= pos[1] < self.width:
            return True
        return False

    def sink_after50years(self):
        new_map = copy.deepcopy(self.earth_map)
        maintain_lands = []
        DXS = [-1, 1, 0, 0]
        DYS = [0, 0, -1, 1]
        for pos in self.find_land():
            x, y = pos
            land_cnt = 0
            for i in range(4):
                nx = x + DXS[i]
                ny = y + DYS[i]
                if self.in_range([nx, ny]) and self.earth_map[nx][ny] == 'X':
                    land_cnt += 1
            if land_cnt < 2:
                new_map[x][y] = '.'
            else:
                maintain_lands.append([x, y])
        return new_map, maintain_lands

    def draw_newmap(self) -> None:
        new_map, lands = self.sink_after50years()
        lands.sort()
        xmin = lands[0][0]
        xmax = lands[-1][0]
        lands.sort(key=lambda x: x[1])
        ymin = lands[0][1]
        ymax = lands[-1][1]

        for i in range(xmin, xmax+1):
            print(''.join(new_map[i][ymin:ymax+1]))


def init_data():
    height, width = map(int, input().split())
    earth_map = list([l for l in input().strip()] for _ in range(height))

    return earth(height, width, earth_map)


if __name__ == '__main__':
    earth_info = init_data()
    earth_info.draw_newmap()
