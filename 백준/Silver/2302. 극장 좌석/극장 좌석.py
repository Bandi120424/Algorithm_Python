import sys
input = sys.stdin.readline


def init_data():
    total_seats = int(input())
    total_vip = int(input())
    vip_seats = [int(input()) for _ in range(total_vip)]

    return total_seats, total_vip, vip_seats


def count_cases(total_seats):
    cases = [0]*(total_seats+1)  # cases[n]: n명의 사람이 좌석에 앉는 가짓수
    cases[0] = 1
    cases[1] = 1
    # cases[2] = 2

    for i in range(2, total_seats+1):
        cases[i] = cases[i-1]+cases[i-2]
    return cases


def vip_arrives(total_seats, total_vip, vip_seats):
    cases = count_cases(total_seats)

    if total_vip == 0:
        return cases[-1]

    ctn = 1
    pre_vip = 0
    for vip in vip_seats:
        ctn *= cases[vip-pre_vip-1]
        pre_vip = vip
    ctn *= cases[total_seats-pre_vip]
    return ctn


if __name__ == '__main__':
    total_seats, total_vip, vip_seats = init_data()
    print(vip_arrives(total_seats, total_vip, vip_seats))
