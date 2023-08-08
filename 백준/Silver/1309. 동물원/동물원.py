import sys
input = sys.stdin.readline


class Cage():
    def __init__(self, size) -> None:
        self.size = size

    def construct_cage(self):
        capture = [0]*(self.size+1)
        capture[0] = 1
        capture[1] = 3
        prev_cases = 0
        for i in range(2, self.size+1):
            prev_cases += capture[i-2]
            capture[i] = (capture[i-1] + 2*(1+prev_cases)) % 9901

        return capture[self.size]


if __name__ == "__main__":
    lion_cage = Cage(int(input()))
    print(lion_cage.construct_cage())
