import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
QnA = [list(map(int, input().split())) for _ in range(N)]
numbers = [str(i) for i in range(1, 10)]
possible_cases = list(permutations(numbers, 3))
rmnum = 0
total_case = len(possible_cases)

# 각 case 마다 strike와 ball 갯수가 일치하는지 확인
for i in range(total_case):
    case = possible_cases[i]
    for q in QnA:
        q_num = str(q[0])
        strikes = sum([q_num[j] == case[j] for j in range(3)])
        if strikes != q[1]:
            rmnum += 1
            break
        else:
            ball = len(set(case) & set(
                [q_num[0], q_num[1], q_num[2]])) - strikes
            if ball != q[2]:
                rmnum += 1
                break

print(total_case - rmnum)