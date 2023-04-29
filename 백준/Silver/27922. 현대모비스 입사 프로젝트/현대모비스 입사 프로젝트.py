import sys
from itertools import combinations
input = sys.stdin.readline

total_courses, take_courses = map(int, input().split())
lecture_info_sum1 = []
lecture_info_sum2 = []
lecture_info_sum3 = []

for _ in range(total_courses):
    comm, algo, machine = map(int, input().split())
    lecture_info_sum1.append(comm+algo)
    lecture_info_sum2.append(comm+machine)
    lecture_info_sum3.append(algo+machine)
    
ability_sum1 = sum(sorted(lecture_info_sum1, reverse = True)[:take_courses])
ability_sum2 = sum(sorted(lecture_info_sum2, reverse = True)[:take_courses])
ability_sum3 = sum(sorted(lecture_info_sum3, reverse = True)[:take_courses])

print(max(ability_sum1, ability_sum2, ability_sum3))

