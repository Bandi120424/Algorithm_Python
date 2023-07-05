import sys
input = sys.stdin.readline


def init_data():
    size = int(input())
    income_map = [list(map(int, input().split())) for _ in range(size)]
    return size, income_map


# sum_arr[i, j] = arr[0][0] ~ arr[i-1][j-1] 까지의 합
def prefix_sum(size, arr):
    sum_arr = [[0 for _ in range(size+1)] for _ in range(size+1)]
    for i in range(1, size+1):
        for j in range(1, size+1):
            sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i-1][j] + \
                sum_arr[i][j-1]-sum_arr[i-1][j-1]
    return sum_arr


def area_sum(pos1, pos2, sum_arr):
    x1, y1 = pos1
    x2, y2 = pos2
    return sum_arr[x2+1][y2+1] - sum_arr[x1][y2+1] - sum_arr[x2+1][y1] + sum_arr[x1][y1]


def max_income(size, income_map=None):
    if income_map == None:
        raise Exception("Input is None")

    max_val = max(max(row) for row in income_map)
    sum_arr = prefix_sum(size, income_map)
    # income_map의 각 위치를 돌면서 누적합을 구함 => 최대소득 업데이트
    if size > 1:
        for x in range(size):
            for y in range(size):
                k = min(size-x, size-y)-1
                while k > 0:
                    max_val = max(max_val, area_sum(
                        [x, y], [x+k, y+k], sum_arr))
                    k -= 1

    return max_val


if __name__ == '__main__':
    size, income_map = init_data()
    print(max_income(size, income_map))
