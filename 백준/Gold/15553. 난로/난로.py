import sys
input = sys.stdin.readline


def init_data():
    total_friends, total_matches = map(int, input().split())
    arrival_time = [int(input()) for _ in range(total_friends)]
    return total_friends, total_matches, arrival_time


def compute_diff(arrival_time, total_friends):
    time_diff = [arrival_time[i+1] - arrival_time[i]
                 for i in range(total_friends-1)]
    return sorted(time_diff)


def heating_time(total_friends, total_matches, arrival_time):
    if total_matches == 1:
        return arrival_time[-1]+1-arrival_time[0]

    time_diff = compute_diff(arrival_time, total_friends)
    return sum(time_diff[:total_friends - total_matches]) + total_matches


total_friends, total_matches, arrival_time = init_data()
print(heating_time(total_friends, total_matches, arrival_time))
