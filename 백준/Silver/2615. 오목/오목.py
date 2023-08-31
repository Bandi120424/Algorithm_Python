import sys
input = sys.stdin.readline

SIZE: int = 19
def init_data():
    boards = [list(map(int, input().split())) for _ in range(SIZE)]
    return boards

class Board():
    def __init__(self, board_map = None, size: int = SIZE) -> None:
        if board_map == None:
            raise Exception(f"{self.__class__} {sys._getframe().f_code.co_name}: there is no board_map")
        self.board_map = board_map
        self.size = size
        
    def in_range(self, pos = None):
        if pos == None:
            raise Exception(f"{self.__class__} {sys._getframe().f_code.co_name}: there is no pos")
    
        if 0 <= pos[0] < SIZE and 0 <= pos[1] < SIZE:
            return True
        return False 
    
    def line_check(self, pos = None, color: int=1):
        if pos == None:
            raise Exception(f"{self.__class__} {sys._getframe().f_code.co_name}: there is no pos")
    
        DXS = [-1, 0, 1, 1]
        DYS = [1, 1, 0, 1]
        x, y = pos
        for i in range(4): #왼쪽 상단부터 오른쪽 하단으로 탐색
            cnt = 1
            nx = x+DXS[i]
            ny = y+DYS[i]
            
            while self.in_range([nx, ny]) and self.board_map[nx][ny] == color:
                cnt += 1
                
                if cnt == 5:
                    if self.in_range([nx+DXS[i], ny+DYS[i]]) and self.board_map[nx+DXS[i]][ny+DYS[i]] == color:
                        break
                    if self.in_range([x-DXS[i], y-DYS[i]]) and self.board_map[x-DXS[i]][y-DYS[i]] == color:
                        break

                    return True, color, [x+1, y+1]
                
                nx += DXS[i]
                ny += DYS[i]

        return False, 0, []
            
    def winner_check(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board_map[i][j] != 0:
                    flag, color, pos = self.line_check([i, j], self.board_map[i][j])
                    if flag == True:
                        print(color)
                        print(*pos)
                        return 
        print(0)
        return 

if __name__ == '__main__':
    boards = Board(init_data())
    boards.winner_check()