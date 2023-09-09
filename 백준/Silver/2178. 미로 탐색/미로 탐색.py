import sys
import copy 
from collections import deque
input = sys.stdin.readline

class Maze():
    def __init__(self, height, width, maze_info) -> None:
        self.height = height
        self.width = width
        self.maze_info = maze_info
        
    def in_range(self, pos):
        if 0 <= pos[0] < self.height and 0 <= pos[1] < self.width:
            return True 
        return False 
    
    def is_valid_pos(self, pos):
        if self.in_range(pos) and self.maze_info[pos[0]][pos[1]] == 1:
            return True 
        return False 
        
    def mininum_path(self):        
        DIRECTIONS = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        
        maze_dist = copy.deepcopy(self.maze_info)
        visited = [[False]*self.width for _ in range(self.height)] 
        queue = deque([])
        queue.append([0, 0])
        visited[0][0] = True 
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + DIRECTIONS[i][0]
                ny = y + DIRECTIONS[i][1]
                if self.is_valid_pos([nx, ny]) and visited[nx][ny] == False:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    maze_dist[nx][ny] = maze_dist[x][y] + 1
        return maze_dist[self.height-1][self.width-1]
                     
def init_data():
    height, width = map(int, input().split())
    maze_info = []
    for _ in range(height):
        row = [x for x in input().strip()]
        maze_info.append(list(map(int, row)))
    return Maze(height, width, maze_info)

if __name__ == "__main__":
    maze = init_data()
    print(maze.mininum_path())