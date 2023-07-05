import sys
import heapq
input = sys.stdin.readline


def init_data():
    total_visit = int(input())
    visit_info = [list(map(int, input().split())) for _ in range(total_visit)]

    return total_visit, visit_info


def give_presents_heap(visit_info):
    present = []
    value = []
    for info in visit_info:
        if info[0] == 0:
            value.append(-heapq.heappop(present)
                         ) if present else value.append(-1)
            continue
        for ele in info[1:]:
            heapq.heappush(present, -ele)

    for val in value:
        print(val)


if __name__ == '__main__':
    total_visit, visit_info = init_data()
    give_presents_heap(visit_info)
