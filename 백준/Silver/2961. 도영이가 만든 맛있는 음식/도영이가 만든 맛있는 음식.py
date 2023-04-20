import sys
from itertools import combinations
input = sys.stdin.readline

# init data
ingredients_num = int(input())
ingredients_info = []
for _ in range(ingredients_num):
    # sour, bitter = map(int, input().split())
    ingredients_info.append(list(map(int, input().split())))

all_cases = [combinations(ingredients_info, i)
             for i in range(1, ingredients_num+1)]
diff_val = float("inf")
for case in all_cases:
    for food in case:
        food_sour, food_bitter = 1, 0
        for sour, bitter in food:
            food_sour *= sour
            food_bitter += bitter
        diff_val = min(diff_val, abs(food_sour - food_bitter))
 
print(diff_val)
