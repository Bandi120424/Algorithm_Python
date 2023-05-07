import sys
input = sys.stdin.readline

input_num = int(input())

pinary_num = [0] * (91)
pinary_num[1] = 1
pinary_num[2] = 1

for i in range(3, input_num+1):
    pinary_num[i] = pinary_num[i-1]+pinary_num[i-2]

print(pinary_num[input_num])
