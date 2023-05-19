import sys
input = sys.stdin.readline

total_students = int(input())
expect_rank = [int(input().strip()) for _ in range(total_students)]
actual_rank = sorted(expect_rank)


def compute_voc(expect, actual):
    score = 0
    for idx in range(1, total_students+1):
        score += abs(idx - actual[idx-1])
        # print("idx, score", idx, score)
    return score


print(compute_voc(expect_rank, actual_rank))
