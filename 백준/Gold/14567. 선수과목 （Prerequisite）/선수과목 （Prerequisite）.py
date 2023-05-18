import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def init_data():
    total_subjects, total_preq = map(int, input().split())
    sub_relation = defaultdict(list)
    degree = [0]*(total_subjects+1)
    for _ in range(total_preq):
        pre, target = map(int, input().split())
        sub_relation[pre].append(target)
        degree[target] += 1

    return total_subjects, degree, sub_relation


def min_semester_to_finish(total_subjects, degree, sub_relation):
    sem_ctn = [0 for _ in range(total_subjects+1)]
    queue = deque()
    for sub in range(1, total_subjects+1):
        if degree[sub] == 0:
            queue.append([sub, 1])
            sem_ctn[sub] = 1

    while queue:
        cur_sub, taken_pre = queue.popleft()
        for new_sub in sub_relation[cur_sub]:
            degree[new_sub] -= 1
            if degree[new_sub] == 0:
                queue.append([new_sub, taken_pre+1])
                sem_ctn[new_sub] = taken_pre+1

    return sem_ctn[1:]


if __name__ == '__main__':
    total_subjects, degree, sub_relation = init_data()
    print(*min_semester_to_finish(total_subjects, degree, sub_relation))
