import sys
import copy
from collections import deque
input = sys.stdin.readline

'''
1s : 그대로
2s : 모든 곳에 폭탄 설치
3s : 0s 설치 폭탄 폭발
4s : 모든 곳에 폭탄 설치 == 2s
5s : 2s 설치 폭탄 폭발
6s : == 2s
7s : == 3s
8s : == 2s
9s : == 5s

# 1s [2s 3s 2s,5s] 반복    
1s : n == 1
2s : n%2 == 0
3s : n%4 == 3
5s : n!= 1 and n%4 == 1

'''


class Board:
    def __init__(self, height: int = 0, width: int = 0, board_map=None):
        self.height = height
        self.width = width
        if board_map == None:
            raise Exception(
                f"{self.__class__} {sys._getframe().f_code.co_name}: board_map is None")
        self.board_map = board_map

    def in_range(self, pos):
        if 0 <= pos[0] < self.height and 0 <= pos[1] < self.width:
            return True
        return False

    def bomb_arrangement(self, board_map=None):
        if board_map == None:
            raise Exception(
                f"{self.__class__} {sys._getframe().f_code.co_name}: board_map is None")
        bomb_pos = []
        for i in range(self.height):
            for j in range(self.width):
                if board_map[i][j] == 'O':
                    bomb_pos.append([i, j])
        return bomb_pos

    def explosion(self, bomb_list=None):
        if bomb_list == None:
            raise Exception(
                f"{self.__class__} {sys._getframe().f_code.co_name}: input is None")
        filled_board = [['O']*self.width for _ in range(self.height)]
        DX = [-1, 0, 1, 0]
        DY = [0, 1, 0, -1]
        for x, y in bomb_list:
            filled_board[x][y] = '.'
            for i in range(4):
                nx, ny = x+DX[i], y+DY[i]
                if self.in_range([nx, ny]):
                    filled_board[nx][ny] = '.'

        return filled_board

    def simulate(self, time: int = 0):

        if time % 2 == 0:
            return [['O']*self.width for _ in range(self.height)]

        bomb_pos = self.bomb_arrangement(self.board_map)
        if time % 4 == 3:
            return self.explosion(bomb_pos)
        if time != 1 and time % 4 == 1:
            updated_bomb_pos = self.bomb_arrangement(self.explosion(bomb_pos))
            return self.explosion(updated_bomb_pos)

        return self.board_map  # if time == 1


def init_data():
    height, width, time = map(int, input().split())
    board = [[x for x in input().strip()] for _ in range(height)]
    return Board(height, width, board), time


if __name__ == '__main__':
    board, time = init_data()
    updated_board = board.simulate(time)

    for i in updated_board:
        print(''.join(i))
