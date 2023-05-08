import sys
input = sys.stdin.readline

val = input().strip('\n').split('-')

ans = sum(list(map(int, val[0].split('+'))))
for i in range(1, len(val)):
    add_val = sum(list(map(int, val[i].split('+'))))
    ans -= add_val

print(ans)