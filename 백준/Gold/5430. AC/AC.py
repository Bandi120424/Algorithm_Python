import sys
from collections import deque 
import re
input = sys.stdin.readline


def reverse_op(target_list):
    return list(reversed(target_list))


def delete_op(target_list, reverse_flag):
    if reverse_flag == True:
        target_list.pop()
    if reverse_flag == False:
        target_list.popleft()
    return target_list

def format_to_print(target_list):
    return "["+",".join(target_list)+"]"

test_cases_num = int(input())
for i in range(test_cases_num):
    func_list = input().strip()
    func_list = [f for f in func_list.replace("RR", '')]
    input_num = int(input())
    input_list = deque(input().strip()[1:-1].split(','))

    if func_list.count('D') > input_num:
        print('error')
    else:
        result = input_list.copy()
        reverse_flag = False

        for f in func_list:
            if f == 'R':
                reverse_flag = not reverse_flag
            if f == 'D':
                result = delete_op(result, reverse_flag)
        
        if reverse_flag:
            output = reverse_op(result)  
        else:
            output = list(result)

        print(format_to_print(output))
