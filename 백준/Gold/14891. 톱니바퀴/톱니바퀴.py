import sys
from collections import deque
input = sys.stdin.readline

def init_data():
    gears = {}
    for i in range(1, 5):
        gears[i] = deque((map(int, input().strip())))
        
    actions = []
    for _ in range(int(input())):
        actions.append(list(map(int, input().split())))
        
    return gears, actions        

def rotate_clockwise(gears, gear_num:int=1, direction: int=1):
    # if gears==None:
    #     raise Exception("gears is None")

    if gear_num > 4 or gears[gear_num - 1][2] == gears[gear_num][6]:
        return

    if gears[gear_num - 1][2] != gears[gear_num][6]:
        rotate_clockwise(gears, gear_num + 1, -direction)
        gears[gear_num].rotate(direction)


def rotate_counterclockwise(gears, gear_num:int=1, direction: int=1):
    # if gears==None:
    #     raise Exception("gears is None")

    if gear_num < 1 or gears[gear_num][2] == gears[gear_num + 1][6]:
        return

    if gears[gear_num][2] != gears[gear_num + 1][6]:
        rotate_counterclockwise(gears, gear_num - 1, -direction)
        gears[gear_num].rotate(direction)
        
#def get_score():

gears, actions = init_data()

for i in range(len(actions)):
    gear_num, direction = actions[i]    
    rotate_clockwise(gears, gear_num + 1, -direction)
    rotate_counterclockwise(gears, gear_num - 1, -direction)
    gears[gear_num].rotate(direction)


score = 0
for i in range(4):
    score += gears[i + 1][0] * (2 ** i)

print(score)

