import sys
input = sys.stdin.readline


class Farm():
    def __init__(self, product_per_unit: int = 0, farm_info=None) -> None:
        self.product_per_unit = product_per_unit
        if farm_info == None:
            raise Exception(
                f"{self.__class__} {sys._getframe().f_code.co_name}: farm_info is None")
        self.farm_info = farm_info

    def farm_size(self):
        # 가로, 세로로 제일 긴 변의 인덱스를 찾음
        height_idx = [0]  # 임의로 제일 첫번째 변을 세로로 가정
        width_idx = []
        vertical = True
        for i in range(1, 6):
            if self.farm_info[i][0] != self.farm_info[i-1][0]:
                vertical = False if vertical else True

            height_idx.append(i) if vertical else width_idx.append(i)

        def max_length(self, idx):
            max_idx, max_length = 0, 0
            for i in idx:
                if self.farm_info[i][1] > max_length:
                    max_length = self.farm_info[i][1]
                    max_idx = i
            return max_idx, max_length

        max_h_idx, max_h = max_length(self, height_idx)
        max_w_idx, max_w = max_length(self, width_idx)

        # max_h*max_w - small_square
        small_square = 1
        for i in range(6):
            if i not in set([max_h_idx, max_w_idx, (max_h_idx+1) % 6, (max_w_idx+1) % 6, (max_h_idx-1) % 6, (max_w_idx-1) % 6]):
                small_square *= self.farm_info[i][1]

        return max_h*max_w - small_square

    def productivity(self):
        return self.product_per_unit*self.farm_size()


def init_data():
    product_per_unit = int(input())
    farm_info = []
    for _ in range(6):
        farm_info.append(list(map(int, input().split())))
    return Farm(product_per_unit, farm_info)


if __name__ == "__main__":
    # 참외밭 넓이 = 큰 직사각형 넓이 - 작은 직사각형의 넓이 (긴 변하고 맞닿아 있지 않은 것)
    farm = init_data()
    print(farm.productivity())
