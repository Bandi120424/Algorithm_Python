from itertools import combinations
from collections import defaultdict
from bisect import bisect_left, bisect_right


def info_to_dict(information: list):
    """information에 대해 가능한 모든 경우의 query를 생성 
    ex) information = "java backend junior pizza 150" 
    infodict의 key값 = {'java - junior pizza', 'java - - pizza' , ... 등}
    infordict[key] = 150 

    Args:
        information (list): 지원자 정보 

    Returns:
        dictionary: key값: 지원자 정보를 기반하여 가능한 모든 query, value: key값 query에 해당되는 지원자의 score (오름차순 정렬)
    """
    infodict = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        for i in range(5):
            cases = list(combinations([0, 1, 2, 3], i))
            for c in cases:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                infodict[key].append(score)

    # 각 infodict의 value들을 오름차순으로 sort
    for value in infodict.values():
        value.sort()

    return infodict


def solution(information, queries):
    """information의 지원자 정보를 바탕으로 queries의 각 문의조건 해당하는 지원자 수를 출력 

    Args:
        information (list): 지원자 정보
        queries (list): 개발팀이 궁금해하는 문의조건

    Returns:
        list : 각 문의조건에 해당하는 사람들의 숫자를 담은 배열
    """
    answer = []
    infodict = info_to_dict(information)

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in infodict:
            target_list = infodict[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    return answer


# print(solution(["java backend junior pizza 150", "java backend junior chicken 80"],
#                ["java and backend and junior and pizza 100"]))

test_list = [i for i in range(10)]
# bisect_left: all(val < x for val in test_list[0 : i]를 만족하는 i
# bisect_right: all(val >= x for val in test_list[i : len(test_list)]) 를 만족하는 i
print("bisect_left(test_list, 3)", bisect_left(test_list, 3))
print("bisect_right(test_list, 3)", bisect_right(test_list, 3))
