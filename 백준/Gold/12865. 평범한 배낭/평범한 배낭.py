import sys
input = sys.stdin.readline

product_num, weight_bound = map(int, input().split())
product_list = [list(map(int, input().split())) for _ in range(product_num)]
baggage = [0] * (weight_bound+1)

for idx, (prod_weight, value) in enumerate(product_list):
    for bag_weight in range(weight_bound, prod_weight-1, -1):
        baggage[bag_weight] = max(
            baggage[bag_weight], baggage[bag_weight-prod_weight]+value)

print(baggage[weight_bound])
