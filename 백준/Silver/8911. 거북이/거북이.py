import sys
input = sys.stdin.readline

T = int(input())
cases = [input() for _ in range(T)]
#direction = N:0, E:1, S:2, W:3 
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
 
def move(pos, cur_dir, order):
    x, y = pos[0], pos[1]
    if order == 'F':
        return [x+dx[cur_dir], y+dy[cur_dir]]
    else: #order == 'B'
        return [x+dx[(cur_dir+2)%4], y+dy[(cur_dir+2)%4]]

def change_dir(cur_dir, order):
    if order == 'L':
        return (cur_dir - 1)%4
    else: #order == 'R'
        return (cur_dir + 1)%4
        
    
for i in range(T):
    path = [[0, 0]]
    j, dir = 0, 0
    for s in cases[i]:
        if s in {'F', 'B'}:
            path.append(move(path[j], dir, s))
            j += 1
        else: 
            dir = change_dir(dir, s)
    
    path_x = [i[0] for i in path]
    path_y = [i[1] for i in path]
    
    width = max(path_x) - min(path_x)
    height = max(path_y) - min(path_y)
    
    print(width*height)
    
        
        
    