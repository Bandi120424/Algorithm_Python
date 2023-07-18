total_days, minimum_credit = map(int, input().split())
credits = [list(map(int, input().split())) for _ in range(2)]
cnt = 0


def do_mision(days, earn, prev):
    global cnt
    if days == total_days:
        if earn >= minimum_credit:
            cnt += 1
        return

    for nr, nc in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]:
        if nc == prev:
            do_mision(days+1, earn+credits[nr][nc]//2, nc)
        else:
            do_mision(days+1, earn+credits[nr][nc], nc)


do_mision(0, 0, -1)
print(cnt)