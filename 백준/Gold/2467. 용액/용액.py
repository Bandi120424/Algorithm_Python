import sys
input = sys.stdin.readline


def init_data():
    total_solution = int(input())
    solutions = list(map(int, input().split()))

    return total_solution, solutions


def make_solution(total_solution, solutions):

    left = 0
    right = total_solution-1
    result = abs(solutions[left]+solutions[right])
    pair = [solutions[left], solutions[right]]

    while left < right:
        new_comb = solutions[right]+solutions[left]

        if abs(new_comb) < result:
            result = abs(new_comb)
            pair = [solutions[left], solutions[right]]
            if result == 0:
                return pair

        if new_comb < 0:
            left += 1
        else:
            right -= 1

    return pair


if __name__ == '__main__':
    total_solution, solutions = init_data()
    print(*make_solution(total_solution, solutions))
