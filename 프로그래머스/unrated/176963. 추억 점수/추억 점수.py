def point(name, yearning):
    p_dic = {}
    for i in range(len(name)):
        p_dic[name[i]] = yearning[i]
    return p_dic

def solution(name, yearning, photo):
    answer = []
    p_dic = point(name, yearning)
    for pic in photo:
        pt = 0
        for n in pic:
            if n in name:
                pt += p_dic[n]
        answer.append(pt)
    return answer