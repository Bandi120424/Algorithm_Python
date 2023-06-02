import sys
input = sys.stdin.readline


def init_data():
    val = input().strip()
    target = [x for x in input().strip()]

    return val, target


def target2val(target, val):
    while target:
        last_char = target.pop()

        if last_char == 'B':
            target.reverse()

        if ''.join(target) == val:
            return 1

    return 0


def ctn_diff(val, target):
    diff_A = target.count('A') - val.count('A')
    diff_B = target.count('B') - val.count('B')

    if diff_A < 0 or diff_B < 0:
        return False

    return True


if __name__ == '__main__':
    val, target = init_data()
    if ctn_diff(val, target) == False:
        print(0)
        exit()

    print(target2val(target, val))
