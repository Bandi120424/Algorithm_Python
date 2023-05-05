import sys
from collections import deque 
input = sys.stdin.readline

def init_data():
    func_list = input().strip()
    func_list = [f for f in func_list.replace("RR", '')]
    input_num = int(input())
    input_list = deque(input().strip()[1:-1].split(','))
    
    return func_list, input_num, input_list 

def reverse_op(target_list=None):
    if target_list == None:
        raise Exception("reverse_op: input is None")
    return list(reversed(target_list))

def delete_op(target_list=None, reverse_flag: bool=False):
    if target_list == None:
        raise Exception("delete_op: input is None")
    if reverse_flag == True:
        target_list.pop()
    if reverse_flag == False:
        target_list.popleft()
    return target_list

def format_to_print(target_list=None):
    if target_list == None:
        raise Exception("format_to_print: input is None")
    return "["+",".join(target_list)+"]"

def operations_AC(func_list=None, input_num: int=0, input_list=None):
    if (func_list == None) or (input_list==None):
        raise Exception("operations_AC: input is None")
    
    if func_list.count('D') > input_num:
        return 'error'

    reverse_flag = False
    for f in func_list:
        if f == 'R':
            reverse_flag = not reverse_flag
        if f == 'D':
            input_list = delete_op(input_list, reverse_flag)
    
    if reverse_flag:
        return format_to_print(reverse_op(input_list))
    
    return format_to_print(list(input_list))
    
test_cases_num = int(input())
for i in range(test_cases_num):
    func_list, input_num, input_list = init_data()
    print(operations_AC(func_list, input_num, input_list))
