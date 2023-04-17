# https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

meeting_num = int(input())
meeting_info = [list(map(int, input().split())) for _ in range(meeting_num)]

meeting_info.sort(key=lambda x: (x[1], x[0]))

meeting_cnt = 1
end_time = meeting_info[0][1]
for i in range(1, meeting_num):
    if end_time <= meeting_info[i][0]:
        meeting_cnt += 1
        end_time = meeting_info[i][1]

print(meeting_cnt)