import sys
input = sys.stdin.readline


def init_data():
    total_candidates = int(input())
    candidates = [list(map(int, input().split()))
                  for _ in range(total_candidates)]
    return total_candidates, sorted(candidates)


def max_pick(total_candidates, candidates):
    cnt = 1
    _, interview = candidates[0]
    for i in range(1, total_candidates):
        if candidates[i][1] < interview:
            cnt += 1
            interview = candidates[i][1]
            continue
    return cnt


if __name__ == '__main__':
    test_case = int(input())
    for _ in range(test_case):
        total_candidates, candidates = init_data()
        print(max_pick(total_candidates, candidates))
