import sys
input = sys.stdin.readline


class visitor_info():
    def __init__(self, days, interval, visitors) -> None:
        self.days = days
        self.interval = interval
        self.visitors = visitors


def init_data():
    days, interval = map(int, input().split())
    visitors = list(map(int, input().split()))

    return visitor_info(days, interval, visitors)


def max_visitors(visit_info):

    days = visit_info.days
    interval = visit_info.interval
    visitors = visit_info.visitors

    if interval == 1:
        max_visit = max(visitors)
        return max_visit, visitors.count(max_visit)

    # visit_sum[i]: i를 시점으로 하여 interval 기간에 방문한 방문자수
    visit_sum = [0 for _ in range(days-interval+1)]
    visit_sum[0] = sum(visitors[:interval])
    for i in range(1, days-interval+1):
        visit_sum[i] = visit_sum[i-1] - visitors[i-1] + visitors[i-1+interval]

    max_visit = max(visit_sum)
    return max_visit, visit_sum.count(max_visit)


if __name__ == '__main__':
    visit_info = init_data()
    max_visit, interval_cnt = max_visitors(visit_info)
    if max_visit == 0:
        print("SAD")
        exit()

    print(max_visit)
    print(interval_cnt)
