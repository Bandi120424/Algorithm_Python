import sys
from collections import deque
input = sys.stdin.readline

class bracket():
    def __init__(self, length: int = 0, target: str = "") -> None:
        self.length = length
        self.target = target
        self.LEFT = 1
        self.RIGHT = -1
        
    def count_bracket(self):
        ctn = 0
        min_ctn, max_ctn = 0, 0
        
        for b in self.target:
            if b == "(":
                ctn += self.LEFT
            elif b == ")":
                ctn += self.RIGHT
            
            min_ctn = min(min_ctn, ctn)
            max_ctn = max(max_ctn, ctn)
        
        return ctn, min_ctn, max_ctn 
    
    def count_days(self) -> int:
        ctn, min_ctn, max_ctn = self.count_bracket()
        
        if self.length % 2 == 1 or ctn != 0:
            return -1
        
        return max(max_ctn, abs(min_ctn))
    
    
def init_data():
    length = int(input())
    target = input().strip()
    return bracket(length, target)

if __name__ == "__main__":
    bracket_info = init_data()
    print(bracket_info.count_days())
        
        