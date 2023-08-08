import sys
input = sys.stdin.readline


class Cage():
    def __init__(self, size: int = 1) -> None:
        self.size = size
        self.capture = [0]*(self.size+1)
        self.capture[0] = 1
        self.capture[1] = 3

    def construct_cage(self):
        prev_cases = 0
        for i in range(2, self.size+1):
            prev_cases += self.capture[i-2]
            self.capture[i] = (self.capture[i-1] + 2*(1+prev_cases)) % 9901

    def ways_to_capture(self, idx: int = 1):
        return self.capture[idx]


if __name__ == "__main__":
    lion_cage = Cage(int(input()))
    lion_cage.construct_cage()
    print(lion_cage.ways_to_capture(lion_cage.size))
