import sys
from collections import deque
input = sys.stdin.readline

total_truck, bridge_len, max_weight = map(int, input().split())
trucks = deque([int(x) for x in input().split()])

bridge = deque([0] * bridge_len)
time = 0
on_bridge_weight = 0
while True:
    out = bridge.popleft()
    on_bridge_weight -= out

    if trucks:
        if on_bridge_weight + trucks[0] <= max_weight:
            bridge.append(trucks[0])
            on_bridge_weight += trucks[0]
            trucks.popleft()
        else:
            bridge.append(0)
    time += 1

    if not bridge:
        break

print(time)