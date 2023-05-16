import sys
input = sys.stdin.readline


def init_data():
    total_blocks, step_width = map(int, input().split())
    block_dist = list(map(int, input().split()))
    return total_blocks, step_width, block_dist


def update_blocks(total_blocks, step_width, block_dist):

    jump_to_arrive = [0] * total_blocks
    nojump_to_arrive = [0] * total_blocks

    jump_to_arrive[0] = 1
    nojump_to_arrive[0] = 1

    for i in range(1, total_blocks):
        if block_dist[i-1] <= step_width:
            jump_to_arrive[i] = jump_to_arrive[i-1]+1
            nojump_to_arrive[i] = nojump_to_arrive[i-1]+1
        else:  # 점프 없이는 갈 수 없는 경우
            nojump_to_arrive[i] = 1  # 해당 block을 시작점으로 하는 경우만 가능
            jump_to_arrive[i] = nojump_to_arrive[i-1] + 1

    return jump_to_arrive, nojump_to_arrive


if __name__ == '__main__':
    total_blocks, step_width, block_dist = init_data()
    jump_to_arrive, nojump_to_arrive = update_blocks(
        total_blocks, step_width, block_dist)
    print(max(max(jump_to_arrive), max(nojump_to_arrive)))
