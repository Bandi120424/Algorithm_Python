import sys
input = sys.stdin.readline


def init_data():
    expr = input().strip('\n').split('-')
    return expr


def bracket_summation(expr):
    return sum(list(map(int, expr.split('+'))))


if __name__ == "__main__":
    expr = init_data()
    ans = bracket_summation(expr[0])
    for i in range(1, len(expr)):
        ans -= bracket_summation(expr[i])

    print(ans)
