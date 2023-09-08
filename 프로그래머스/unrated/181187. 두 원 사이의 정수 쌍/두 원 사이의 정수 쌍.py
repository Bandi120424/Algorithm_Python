import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2):
        if x < r1:
            lbd = math.sqrt(r1**2-x**2)
            if lbd == int(lbd):
                answer += int(math.sqrt(r2**2-x**2)) - lbd + 1
            else:
                answer += int(math.sqrt(r2**2-x**2)) - int(lbd)
            continue
        answer += int(math.sqrt(r2**2-x**2)) 
            
    answer += r2-r1+1
    answer *= 4    
    
    return answer