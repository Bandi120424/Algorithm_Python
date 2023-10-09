import copy

class Park:
    def __init__(self, park):
        self.park = park
        self.width = len(park[0])
        self.height = len(park)
        self.park_arr = []
        self.init_pos = [0, 0]
        
    def list2array(self):
        for i, row in enumerate(self.park):
            row_arr = []
            for j, c in enumerate(row):
                if c == "S":
                    self.init_pos = [i, j]
                row_arr.append(c)
            self.park_arr.append(row_arr)
    
    def in_range(self, pos):
        if 0 <= pos[0] < self.height and 0 <= pos[1] < self.width:
            return True
        return False 

    def can_move(self, new_pos):
        if self.in_range(new_pos) and self.park[new_pos[0]][new_pos[1]] != "X":
            return True
        return False
        
    def move(self, pos, order):
        direction, iter_time = order[0], int(order[-1])
        new_pos = pos 
        
        for i in range(iter_time):
            if direction == "E":
                new_pos = [new_pos[0], new_pos[1]+1]
            if direction == "W":
                new_pos = [new_pos[0], new_pos[1]-1]
            if direction == "N":
                new_pos = [new_pos[0]-1, new_pos[1]]
            if direction == "S":
                new_pos = [new_pos[0]+1, new_pos[1]]
        
            if not self.can_move(new_pos):
                return pos

        return new_pos
        
    def take_walk(self, routes):
        self.list2array()
        pos = copy.deepcopy(self.init_pos)
        for order in routes:
            pos = self.move(pos, order)
        return pos    
    
def solution(park, routes):
    walk_info = Park(park)
    return walk_info.take_walk(routes)