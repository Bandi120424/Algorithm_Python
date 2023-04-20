import sys
input = sys.stdin.readline

# init data
sensor_num = int(input())
base_station_num = int(input())
sensor_pos = sorted(list(map(int, input().split())))


# def min_transmission_area():
if base_station_num >= sensor_num:  # 각 센서에 집중국 설치
    print(0)
    sys.exit()

distance = []
for i in range(1, sensor_num):
    distance.append(sensor_pos[i] - sensor_pos[i-1])

distance.sort(reverse=True)
for _ in range(base_station_num-1):
    distance.pop(0)

print(sum(distance))


# print(min_transmission_area())
