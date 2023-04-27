import sys
input = sys.stdin.readline

num = int(input())


def is_square(num):
    root_num = num**(0.5)
    if root_num == int(root_num):
        return True
    return False


if is_square(num):
    print(1)
else:
    lagrange_arr = [0] * (num+1)
    for i in range(1, num+1):
        if is_square(i):
            lagrange_arr[i] = 1
            continue
        lagrange_arr[i] = min(lagrange_arr[i-j**2]
                              for j in range(1, int(i**(0.5))+1)) + 1

    print(lagrange_arr[num])
