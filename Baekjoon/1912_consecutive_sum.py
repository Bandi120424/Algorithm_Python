import sys
input = sys.stdin.readline

def init_data():
    num_of_input = int(input())
    numbers = list(map(int, input().split()))
    return [num_of_input, numbers]

def consecutive_sums(num_of_input: int = 0, numbers = None):
    if numbers == None:
        raise KeyError
    consecutive_sum = [0] * num_of_input
    consecutive_sum[0] = numbers[0]
    
    for i in range(1, num_of_input):
        consecutive_sum[i] = max(numbers[i], consecutive_sum[i-1]+numbers[i])
    
    return consecutive_sum

def solution():
    num_of_input, numbers = init_data()
    max_consecutive_sum = max(consecutive_sums(num_of_input, numbers))
    return max_consecutive_sum
    
print(solution())
