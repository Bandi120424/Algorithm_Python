import sys
input = sys.stdin.readline


def init_data():
    total_visit = int(input())
    visit_info = [list(map(int, input().split())) for _ in range(total_visit)]

    return total_visit, visit_info


def give_presents(visit_info):
    present = []
    value = []
    for info in visit_info:
        if info[0] == 0:
            value.append(present.pop()) if present else value.append(-1)
            continue
        present.extend(info[1:])
        present.sort()

    for val in value:
        print(val)


if __name__ == '__main__':
    total_visit, visit_info = init_data()
    give_presents(visit_info)
