import sys
from collections import deque
input = sys.stdin.readline


def init_data():
    total_people = int(input())
    relation = [[1 if x == 'Y' else 0 for x in input().strip()]
                for _ in range(total_people)]
    return total_people, relation


def find_connection(relation):
    connection = [[] for _ in range(total_people)]
    for i in range(total_people):
        for j in range(i, total_people):
            if relation[i][j] == True:
                connection[i].append(j)
                connection[j].append(i)

    return connection


def update_connection(start, total_people, connection):
    queue = deque()
    queue.append([start, 0])
    visited = [False]*total_people
    visited[start] = True
    friend_count = 0

    while queue:
        person, ctn = queue.popleft()
        if ctn > 1:
            continue

        for friend in connection[person]:
            if visited[friend] == False and relation[person][friend]:
                friend_count += 1
                visited[friend] = True
                queue.append([friend, ctn+1])
    return friend_count


if __name__ == '__main__':
    total_people, relation = init_data()

    max_friend = 0
    connection = find_connection(relation)
    for i in range(total_people):
        max_friend = max(max_friend, update_connection(
            i, total_people, connection))

    print(max_friend)
