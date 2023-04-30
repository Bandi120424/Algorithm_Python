import sys
input = sys.stdin.readline

test_case_num = int(input())
pair_ctn = []
for _ in range(test_case_num):
    num_A, num_B = map(int, input().split())
    set_A = list(map(int, input().split()))
    set_B = sorted(list(map(int, input().split())), reverse=True)

    ctn = 0
    for ele_a in set_A:
        for i in range(num_B):
            if ele_a > set_B[i]:
                ctn += num_B-i
                break
    pair_ctn.append(ctn)

for pair in pair_ctn:
    print(pair)
