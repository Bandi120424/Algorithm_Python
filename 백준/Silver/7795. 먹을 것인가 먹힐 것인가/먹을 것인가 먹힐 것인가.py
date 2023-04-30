import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    ret = 0
    i = 0
    for a in A:
        while i < m and a > B[i]:
            i += 1
        ret += i
    return ret

T = int(input())
for _ in range(T):
    print(main())