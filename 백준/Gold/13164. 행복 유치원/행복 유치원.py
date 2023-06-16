import sys
input = sys.stdin.readline


def init_data():
    kids, teams = map(int, input().split())
    heights = list(map(int, input().split()))

    return kids, teams, heights

# 간격이 큰 두 사람을 최대한 분리


def cost(kids, teams, heights):
    intervals = []
    for i in range(1, kids):
        intervals.append(heights[i]-heights[i-1])
    intervals.sort(reverse=True)

    return sum(intervals[teams-1:])


if __name__ == '__main__':
    kids, teams, heights = init_data()
    print(cost(kids, teams, heights))
