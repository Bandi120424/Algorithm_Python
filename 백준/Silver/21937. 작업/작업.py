import sys
input = sys.stdin.readline


class flowchart():
    def __init__(self, num_of_work: int = 0, chart=None) -> None:
        self.num_of_work = num_of_work
        self.chart = chart


def init_data():
    num_of_work, work_order = map(int, input().split())
    work_info = [[] for _ in range(num_of_work+1)]
    for _ in range(work_order):
        pre, post = map(int, input().split())
        work_info[post].append(pre)
    target = int(input())

    return flowchart(num_of_work, work_info), target


def minimum_workload(work_chart=None, target: int = 0) -> int:

    if work_chart == None:
        raise Exception("There is no flowchart")
    if target == 0:
        raise Exception("The target is wrong")

    visited = [False]*(work_chart.num_of_work+1)
    visited[target] = True
    stack = [target]
    cnt = 0

    while stack:
        node = stack.pop()
        for next_node in work_chart.chart[node]:
            if visited[next_node] == False:
                stack.append(next_node)
                visited[next_node] = True
                cnt += 1

    return cnt


if __name__ == "__main__":
    work_chart, target = init_data()
    print(minimum_workload(work_chart, target))
