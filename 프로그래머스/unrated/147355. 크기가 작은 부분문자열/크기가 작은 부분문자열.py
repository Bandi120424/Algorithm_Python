def solution(t, p):
    answer = 0
    num = int(p)
    num_len = len(p)
    for i in range(len(t)-num_len+1):
        if num >= int(t[i:i+num_len]):
            answer += 1
    return answer