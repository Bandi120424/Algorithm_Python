import sys
input = sys.stdin.readline

input_num = int(input())
ops = [0 for _ in range(input_num+1)]

for i in range(2, input_num+1):
    ops[i] = ops[i-1]+1
    if i % 3 == 0:
        ops[i] = min(ops[i], ops[i//3] + 1)
    if i % 2 == 0:
        ops[i] = min(ops[i], ops[i//2] + 1)

print(ops[input_num])
