import sys
input = sys.stdin.readline


def init_data():
    total_dish, sushi_num, dishes_to_eat, coupon_num = map(
        int, input().split())
    belt = [int(input()) for _ in range(total_dish)]

    return total_dish, dishes_to_eat, coupon_num, belt


def count_unique_dish(dishes, coupon_num):
    if coupon_num not in dishes:
        return len(set(dishes))+1
    return len(set(dishes))


def eat_serial_dishes(belt, total_dish, dishes_to_eat, coupon_num):  # 연속한 접시들의 초밥 종류를 카운트
    max_dish = 0
    for dish_idx in range(total_dish):
        end = dish_idx + dishes_to_eat

        if end > total_dish - 1:
            end %= total_dish
            dishes = belt[dish_idx:]+belt[:end]
        else:
            dishes = belt[dish_idx: end]

        max_dish = max(max_dish, count_unique_dish(dishes, coupon_num))

    return max_dish


if __name__ == "__main__":
    total_dish, dishes_to_eat, coupon_num, belt = init_data()
    print(eat_serial_dishes(belt, total_dish, dishes_to_eat, coupon_num))
