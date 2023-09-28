from itertools import combinations

def solution(number):
    answer = 0
    whole_cases = combinations(number, 3)
    for case in whole_cases:
        if sum(case) == 0:
            answer += 1
    return answer