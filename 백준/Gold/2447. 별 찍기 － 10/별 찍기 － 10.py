import sys
input = sys.stdin.readline


''' pattern
***
* *
***

N = 9
*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********

'''


def draw_star(size):
    if size == 3:
        return ['***', '* *', '***']

    arr = draw_star(size//3)
    stars = []

    # 전체를 삼등분으로 나눠서 그림
    # 위
    for i in arr:
        stars.append(i*3)
    # 가운데
    for i in arr:
        stars.append(i+' '*(size//3)+i)
    # 아래
    for i in arr:
        stars.append(i*3)

    return stars


def init_data():
    size = int(input())
    return size


if __name__ == '__main__':
    size = init_data()
    print('\n'.join(draw_star(size)))
