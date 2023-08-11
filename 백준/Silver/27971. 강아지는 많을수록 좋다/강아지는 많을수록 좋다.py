import sys
from collections import deque
input = sys.stdin.readline

'''
f(n) = min(f(n-magic_a), f(n-magic_b)) + 1 
if n-magic_a in intervals and n-magic_b in intervals:
    return -1 
f(magic_a) = f(magic_b) = 1
'''


class magic():
    def __init__(self, magic_a: int = 0, magic_b: int = 0, restrictions=None) -> None:
        self.magic_a = magic_a
        self.magic_b = magic_b
        self.restriction = []
        if restrictions != None:
            for interval in restrictions:
                self.restriction.extend(
                    [i for i in range(interval[0], interval[1]+1)])
        self.restriction = set(self.restriction)

    def make_puppy(self, target: int = 0) -> int:

        visited = [False] * (target+1)
        for res in self.restriction:
            visited[res] = True

        queue = deque()
        queue.append((0, 0))
        visited[0] = True
        while queue:
            cur_puppy, action_cnt = queue.popleft()
            if cur_puppy == target:
                return action_cnt

            for nxt in [cur_puppy+self.magic_a, cur_puppy+self.magic_b]:
                if nxt <= target and not visited[nxt]:
                    visited[nxt] = True
                    queue.append((nxt, action_cnt+1))
        return -1


def init_data():
    total_puppy, total_interval, magic_a, magic_b = map(int, input().split())
    intervals = [list(map(int, input().split()))
                 for _ in range(total_interval)]

    return magic(magic_a, magic_b, intervals), total_puppy


if __name__ == '__main__':
    magic_info, puppy = init_data()
    print(magic_info.make_puppy(puppy))
