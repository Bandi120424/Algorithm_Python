def solution(targets):
    answer = 0
    bound = 0
    
    for x1, x2 in sorted(targets):
        if bound > x1:
            bound = min(bound, x2)
        else:
            bound = x2
            answer += 1
    return answer