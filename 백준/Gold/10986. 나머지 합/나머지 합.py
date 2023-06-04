import sys
input = sys.stdin.readline


total_num, modulo = map(int, input().split())
numbers = list(map(int, input().split()))
remainder_info = {i:0 for i in range(modulo)}
remainder_info[0] = 1

n_sum = 0
for num in numbers:
    n_sum += num
    remainder_info[n_sum%modulo] += 1

cases_ctn = 0
for i in range(modulo):
    cases_ctn += remainder_info[i]*(remainder_info[i]-1)//2

print(cases_ctn)
