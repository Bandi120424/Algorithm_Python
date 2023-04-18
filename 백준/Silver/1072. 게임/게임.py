import sys
input = sys.stdin.readline


def init_data():
    game_num, win_games = map(int, input().split())

    return game_num, win_games


def game_count(game_num, win_games):

    cur_odds = (100*win_games)//game_num

    if cur_odds >= 99:
        return -1

    lbd = 0
    ubd = game_num
    cnt = game_num

    while lbd <= ubd:
        mid = (lbd+ubd)//2

        if (100*(win_games+mid))//(game_num+mid) > cur_odds:
            cnt = mid
            ubd = mid - 1
        else:
            lbd = mid + 1

    return cnt


def solution():
    game_num, win_games = init_data()
    print(game_count(game_num, win_games))


solution()
