import sys
input = sys.stdin.readline


def init_data():
    size = int(input())

    matrix = []
    for _ in range(size):
        row = list(map(int, input().split()))
        matrix.append(row)

    return size, matrix


def find_second_component(numbers):
    numbers.sort(reverse=True)
    return numbers[1]


def pooling_patch(pool_size, size, matrix):
    new_matrix = []
    for i in range(size//pool_size):
        row = []
        for j in range(size//pool_size):
            row.append(find_second_component([matrix[pool_size*i][pool_size*j], matrix[pool_size*i][pool_size*j+1],
                                              matrix[pool_size*i+1][pool_size*j], matrix[pool_size*i+1][pool_size*j+1]]))
        new_matrix.append(row)

    return new_matrix


def pooling(pool_size, size, matrix):
    new_matrix = pooling_patch(pool_size, size, matrix)
    while len(new_matrix) > 1:
        new_matrix = pooling_patch(2, len(new_matrix), new_matrix)
    return new_matrix[0][0]


if __name__ == '__main__':
    size, matrix = init_data()
    print(pooling(2, size, matrix))
