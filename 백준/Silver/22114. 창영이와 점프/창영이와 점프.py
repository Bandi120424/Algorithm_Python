import sys
input = sys.stdin.readline

total_blocks, step_width = map(int, input().split())
block_dist = list(map(int, input().split()))

blocks_jump = [0] * total_blocks  # i번째 돌에 도달하기까지 거쳐온 block 수
blocks_nojump = [0] * total_blocks

blocks_jump[0] = 1
blocks_nojump[0] = 1

for i in range(1, total_blocks):
    if block_dist[i-1] <= step_width:
        blocks_nojump[i] = blocks_nojump[i-1]+1
        blocks_jump[i] = blocks_jump[i-1]+1
    else:  # 점프 없이는 갈 수 없는 경우
        blocks_nojump[i] = 1
        blocks_jump[i] = blocks_nojump[i-1] + 1

print(max(max(blocks_jump), max(blocks_nojump)))
