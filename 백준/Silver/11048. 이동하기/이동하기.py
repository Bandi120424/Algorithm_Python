import sys
input = sys.stdin.readline

'''
candy[r][c] = max(candy[r-1][c], candy[r-1][c-1], candy[r][c-1]) + candy_map[r][c]
'''


def init_data():
    height, width = map(int, input().split())
    candy_map = [list(map(int, input().split())) for _ in range(height)]
    return height, width, candy_map


def max_candy(height, width, candy_map):
    candy = [[0]*width for _ in range(height)]

    candy[0][0] = candy_map[0][0]
    for i in range(1, width):
        candy[0][i] = candy[0][i-1]+candy_map[0][i]

    for j in range(1, height):
        candy[j][0] = candy[j-1][0]+candy_map[j][0]

    for i in range(1, height):
        for j in range(1, width):
            candy[i][j] = max(candy[i-1][j], candy[i][j-1],
                              candy[i-1][j-1]) + candy_map[i][j]

    return candy[height-1][width-1]


if __name__ == '__main__':
    height, width, candy_map = init_data()
    print(max_candy(height, width, candy_map))
