import sys
input = sys.stdin.readline


def init_data():
    total_people, total_snack = map(int, input().split())
    snacks = list(map(int, input().split()))

    return total_people, total_snack, snacks


def share_snack(total_people, total_snack, snacks):

    result = 0
    left = 1
    right = max(snacks)

    while left <= right:
        mid = (left+right)//2
        cnt = sum([x//mid for x in snacks])
        if cnt >= total_people:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


if __name__ == '__main__':
    total_people, total_snack, snacks = init_data()
    print(share_snack(total_people, total_snack, snacks))
