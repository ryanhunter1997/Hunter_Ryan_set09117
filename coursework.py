#!/usr/bin/python3
from enum import Enum


CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8

WP = 'w'
WQ = 'W'
EC = '_'
BP = 'b'
BQ = 'B'

PLAYERS = Enum("Players", "White Black")

def main():
    print("Python Checkers")
    value_package = dict([("board", init_board()), ("turn_count", 1), ("cur_turn", PLAYERS.Black)])
    board = init_board()
    while True:
        print_board(board)
        jump(value_package, board)

def init_board():
    board=[
            ['w', '_', 'w', '_', 'w', '_', 'w', '_'],
            ['_', 'w', '_', 'w', '_', 'w', '_', 'w'],
            ['w', '_', 'w', '_', 'w', '_', 'w', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'b', '_', 'b', '_', 'b', '_', 'b'],
            ['b', '_', 'b', '_', 'b', '_', 'b', '_'],
            ['_', 'b', '_', 'b', '_', 'b', '_', 'b']]
    return board

def print_board(board):
    print("     1 2 3 4 5 6 7 8\n")
    for i in range (GRID_HEIGHT):
        print(i + 1 ,  "  |", end="")
        for j in range(GRID_WIDTH):
            print(board[i][j] + "|", end="")
        print("")
    print("")



def  jump(value_package, board):
    if value_package["cur_turn"] == PLAYERS.Black:
        print("Black")
        src_x = int(input("Choose a x coord to move from "))
        src_y = int(input("Choose a y coord to move from "))
        dst_x = int(input("Choose a x coord to move to "))
        dst_y = int(input("Choose a y coord to move to "))
    
        src_x = src_x - 1
        src_y = src_y - 1
        dst_x = dst_x - 1
        dst_y = dst_y - 1

        x_diff = abs(src_x - dst_x)
        y_diff = abs(src_x - dst_y)

        mid_x = (src_x + dst_x) // 2
        mid_y = (src_y + dst_y) // 2

    

        if board[src_y][src_x] == '_':
            print('Source cell is empty, try again.')
            return jump(value_package, board)

        if board[dst_y][dst_x] != '_':
            print('Target cell is taken, try again.')
            return jump(value_package, board)
      
        print(src_x, src_y, mid_x, mid_y, dst_x, dst_y)


        if board[mid_y][mid_x] == 'w':
            board[src_y][src_x] = '_'
            board[mid_y][mid_x] = '_'
            board[dst_y][dst_x] = 'b'
            value_package["cur_turn"] = PLAYERS.White
            print_board(board)
            return jump(value_package, board)

        if board[src_y][src_x] == board[mid_y][mid_x]:
            print('Cannot take your own piece')
            return jump(value_package, board)
       


        if src_x == mid_x + 1:
            mid_x = mid_x + 1
            mid_y = mid_y + 1


        if board[mid_y][mid_x] == '_':
            print('No piece to jump over')
            return jump(value_package, board)

        board[dst_y][dst_x] = 'b'
        board[src_y][src_x] = '_'
        
        value_package["cur_turn"] = PLAYERS.White
    
    else:
        
        print("White")
        src_x = int(input("Choose a x coord to move from "))
        src_y = int(input("Choose a y coord to move from "))
        dst_x = int(input("Choose a x coord to move to "))
        dst_y = int(input("Choose a y coord to move to "))
    
        src_x = src_x - 1
        src_y = src_y - 1
        dst_x = dst_x - 1
        dst_y = dst_y - 1
    
        print(src_x, src_y, dst_x, dst_y)

        x_diff = abs(src_x - dst_x)
        y_diff = abs(src_x - dst_y)

        mid_x = (src_x + dst_x) // 2
        mid_y = (src_y + dst_y) // 2


        if board[src_y][src_x] == '_':
            print('Source cell is empty, try again.')
            return jump(value_package, board)

        if board[dst_y][dst_x] != '_':
            print('Target cell is taken, try again.')
            return jump(value_package, board)
       

        if board[mid_y][mid_x] == '_':
            print('No piece to jump over')
            return jump(value_package, board)
      
        print(mid_x, mid_y)

        if src_x == mid_x:
            mid_x = mid_x + 1
            mid_y = mid_y + 1
        
        print (mid_x, mid_y)

        if board[src_y][src_x] == board[mid_y][mid_x]:
            print('Cannot take your own piece')
            return jump(value_package, board)

        board[dst_y][dst_x] = 'w'
        board[src_y][src_x] = '_'
        
        value_package["cur_turn"] = PLAYERS.Black
main()
