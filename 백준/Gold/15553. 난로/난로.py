import sys
input = sys.stdin.readline

total_friends, total_matches = map(int, input().split())
arrival_time = [int(input()) for _ in range(total_friends)]

if total_matches == 1:
    print(arrival_time[-1]+1-arrival_time[0])
    exit()

time_diff = [arrival_time[i+1] - arrival_time[i]
             for i in range(total_friends-1)]

time_diff.sort()
heating_time = sum(
    time_diff[:total_friends - total_matches]) + (total_matches-1)

print(heating_time+1)
