import sys
input = sys.stdin.readline


def init_data():
    total_big_day = int(input())
    big_days = [int(input()) for _ in range(total_big_day)]

    return total_big_day, big_days

# 몇 개의 unique한 주기가 존재하는지


def count_ship(total_big_day, big_days):
    ctn = 0
    for idx in range(1, total_big_day):
        if big_days[idx] == 0:
            continue

        interval = big_days[idx] - big_days[0]
        boat_flag = False
        for j in range(1, total_big_day):
            if big_days[j] == 0:
                continue
            if big_days[j] % interval == 1:  # 주기가 나누어 떨어지는 배들 업데이트
                boat_flag = True
                big_days[j] = 0

        if boat_flag == True:
            ctn += 1

    return ctn


if __name__ == '__main__':
    total_big_day, big_days = init_data()
    print(count_ship(total_big_day, big_days))
