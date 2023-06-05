import sys
from itertools import combinations
input = sys.stdin.readline


def init_data():
    size, max_chicken_store = map(int, input().split())

    city_map = []
    for _ in range(size):
        row = list(map(int, input().split()))
        city_map.append(row)

    return size, max_chicken_store, city_map


def find_house_and_store(size, city_map):
    house = []
    store = []
    for i in range(size):
        for j in range(size):
            if city_map[i][j] == 1:
                house.append([i, j])
            if city_map[i][j] == 2:
                store.append([i, j])
    return house, store


def compute_dist(house, store):
    total_dist = 0
    for r1, c1 in house:
        dist = 999999
        for r2, c2 in store:
            dist = min(dist, (abs(r1-r2)+abs(c1-c2)))
        total_dist += dist
    return total_dist


if __name__ == '__main__':
    size, max_chicken_store, city_map = init_data()
    house, store = find_house_and_store(size, city_map)

    min_distance = 999999
    for case in combinations(store, max_chicken_store):
        min_distance = min(min_distance, compute_dist(house, case))
    print(min_distance)
