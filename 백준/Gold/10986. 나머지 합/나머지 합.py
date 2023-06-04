import sys
input = sys.stdin.readline

def init_data():
    _, modulo = map(int, input().split())
    numbers = list(map(int, input().split()))
    return modulo, numbers

def remainder_info(modulo, numbers):
    remainder_inf = {i:0 for i in range(modulo)}
    remainder_inf[0] = 1

    n_sum = 0
    for num in numbers:
        n_sum += num
        remainder_inf[n_sum%modulo] += 1
    
    return remainder_inf

if __name__ == '__main__':
    modulo, numbers = init_data()
    remainder_inf = remainder_info(modulo, numbers)
    
    cases_ctn = 0
    for i in range(modulo):
        cases_ctn += remainder_inf[i]*(remainder_inf[i]-1)//2

    print(cases_ctn)
