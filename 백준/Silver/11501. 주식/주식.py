import sys
input = sys.stdin.readline

T = int(input())

days = []
stockList = []

for i in range(T):
    days.append(int(input()))
    stockList.append(list(map(int, input().split())))

for i in range(T):
    ans = 0
    stockList[i].reverse()
    while stockList[i]:
        max_val = max(stockList[i])
        max_idx = stockList[i].index(max_val)
        ans += max_val*(len(stockList[i]) - max_idx) - sum(stockList[i][max_idx:])
        stockList[i] = stockList[i][:max_idx]
    print(ans)