#!/usr/bin/python3
from enum import Enum


CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8

Black_Pieces = 12
White_Picees = 12

UP = '~'
WP = 'w'
WQ = 'W'
EC = '_'
BP = 'b'
BQ = 'B'

PLAYERS = Enum("Players", "White Black")

def main():
    print("Python Checkers")
    value_package = dict([("board", init_board()), ("cur_turn", PLAYERS.Black)])
    board = init_board()
    while True:
        print_board(board)
        jump(value_package, board)

def init_board():
    board=[
            ['w', '~', 'w', '~', 'w', '~', 'w', '~'],
            ['~', 'w', '~', 'w', '~', 'w', '~', 'w'],
            ['w', '~', 'w', '~', 'w', '~', 'w', '~'],
            ['~', '_', '~', '_', '~', '_', '~', '_'],
            ['_', '~', '_', '~', '_', '~', '_', '~'],
            ['~', 'b', '~', 'b', '~', 'b', '~', 'b'],
            ['b', '~', 'b', '~', 'b', '~', 'b', '~'],
            ['~', 'b', '~', 'b', '~', 'b', '~', 'b']]
    return board

def print_board(board):
    print("     1 2 3 4 5 6 7 8\n")
    for i in range (GRID_HEIGHT):
        print(i + 1 ,  "  |", end="")
        for j in range(GRID_WIDTH):
            print(board[i][j] + "|", end="")
        print("")
    print("")



def jump(value_package, board, White_Pieces, Black_Pieces):
    if value_package["cur_turn"] == PLAYERS.Black:
        print("Blacks Turn")
      
        exit = input("press any key then hit enter to continue or type exit then hit enter to leave ")
        if exit == "exit":
            exit()
      
        while True:
            try:
                src_x = int(input("Choose a x coord to move from "))
                break
            except:
                print("thats not a number")
              
        while True:
            try:
                src_y = int(input("Choose a y coord to move from "))
                break
            except:
                print("thats not a number")
              
        while True:
            try:
                dst_x = int(input("Choose a x coord to move to "))
                break
            except:
                print("thats not a number")
        
        while True:
            try:
                dst_y = int(input("Choose a y coord to move to "))
                break
            except:
                print("thats not a number")

        src_x = src_x - 1
        src_y = src_y - 1
        dst_x = dst_x - 1
        dst_y = dst_y - 1

        if src_x < 0 or src_x > 7  or src_y < 0 or src_y > 7:
            print("Invalid Source Coord, try again")
            print_board(board)
            return jump(value_package, board)
        
 
        if dst_x < 0 or dst_x > 7  or dst_y < 0 or dst_y > 7:
            print("Destination coord invalid , try again")
            print_board(board)
            return jump(value_package, board)       

        x_diff = abs(src_x - dst_x)
        y_diff = abs(src_x - dst_y)

        mid_x = (src_x + dst_x) // 2
        mid_y = (src_y + dst_y) // 2

    

        if board[src_y][src_x] == EC:
            print('Source cell is empty, try again.')
            return jump(value_package, board)

        if board[dst_y][dst_x] == UP:
            print('Unplayable Cell try again')
            return jump(value_package, board)

        #cannot move more than 2 in any direcetion
        if dst_x > src_x + 2 or dst_x < src_x - 2: 
            print('Move is too long, Try again')
            return jump(value_package, board)

        if dst_y > src_y + 2 or dst_y < src_y - 2:
            print ('Move is too long, Try again')
            return jump(value_package, board)
        
        #moves can only be diaginal
        if dst_x == src_x:
            print('You can only move diagonally, try again')
            return jump(value_package, board)

        if  dst_y == src_y:
            print('You can only move diagonally, try again')
            return jump(value_package, board)

        if board[dst_y][dst_x] != EC:
            print('Target cell is taken, try again.')
            return jump(value_package, board)
       
        if board[src_y][src_x] == BP:
            if dst_y > src_y:
                print("only queens can move backwards")
                return jump(value_package, board)

        #changes board after jumping oppents piece
        if board[mid_y][mid_x] == WP or board[mid_y][mid_x] == WQ:
            if board[src_y][src_x] == BP:
                if dst_y == 0:
                    White_Pieces = White_Pieces - 1
                    board[src_y][src_x] = EC
                    board[mid_y][mid_x] = EC
                    board[dst_y][dst_x] = BQ
                else:  
                    board[src_y][src_x] = EC
                    board[mid_y][mid_x] = EC
                    board[dst_y][dst_x] = BP
                    White_Pieces = White_Pieces - 1
                print_board(board)
                if White_Pieces == 0:
                    print('Black Wins')
                    exit()
            value_package["cur_turn"] = PLAYERS.White
            print_board(board)
            return jump(value_package, board)
        

        if src_x == mid_x + 1:
            mid_x = mid_x + 1
            mid_y = mid_y + 1

        
        #cannot jump and empty cell
        if board[mid_y][mid_x] == EC:
            print('No piece to jump over')
            return jump(value_package, board)
           
        mid_x = mid_x -1
        mid_y = mid_y -1
      

        if board[src_y][src_x] == board[mid_y][mid_x]:
            print('Cannot take your own piece')
            return jump(value_package, board)
      
        if board[src_y][src_x] == BP:
            if dst_y == 0:
                board[src_y][src_x] = EC
                board[dst_y][dst_x] = BQ
            else:
                board[src_y][src_x] = EC
                board[dst_y][dst_x] = BP
                if board[src_y][src_x] == BQ:
                    board[src_y][src_x] = EC
                    board[dst_y][dst_x] = BQ

        value_package["cur_turn"] = PLAYERS.White
        print_board(board)
        return jump(value_package, board)
    
    else:
        print("Whites Turn")
        
        exit = input("press any key then hit enter to continue or type exit then hit enter to leave ")
        if exit == "exit":
            exit()

        while True:
            try:
                src_x = int(input("Choose a x coord to move from "))
                break
            except:
                print("thats not a number")
        
        while True:
            try:
                src_y = int(input("Choose a y coord to move from "))
                break
            except:
                print("thats not a number")

        while True:
            try:
                dst_x = int(input("Choose a x coord to move to "))
                break
            except:
                print("thats not a number")
        
        while True:
            try:
                dst_y = int(input("Choose a y coord to move to "))
                break
            except:
                print("thats not a number")
    
        src_x = src_x - 1
        src_y = src_y - 1
        dst_x = dst_x - 1
        dst_y = dst_y - 1

        x_diff = abs(src_x - dst_x)
        y_diff = abs(src_x - dst_y)

        mid_x = (src_x + dst_x) // 2
        mid_y = (src_y + dst_y) // 2


        if board[src_y][src_x] == EC:
            print('Source cell is empty, try again.')
            return jump(value_package, board)
        
        if board[dst_y][dst_x] == UP:
            print('Unplayable Cell try again')
            return jump(value_package, board)

        #cannot move more than 2 in any direcetion
        if dst_x > src_x + 2 or dst_x < src_x - 2 :
            print('Move is too long, Try again')
            return jump(value_package, board)

        if dst_y > src_y + 2 or dst_y < src_y - 2 :
            print ('Move is too long, Try again')
            return jump(value_package, board)
        
        #moves can only be diaginal
        if dst_x == src_x:
            print('You can only move diagonally, try again')
            return jump(value_package, board)

        if  dst_y == src_y:
            print('You can only move diagonally, try again')
            return jump(value_package, board)

        if board[dst_y][dst_x] != EC:
            print('Target cell is taken, try again.')
            return jump(value_package, board)

        if board[src_y][src_x] == WP:
            if dst_y < src_y:
                print("only queens can move backwards")
                return jump(value_package, board)


        #changes board after jumping oppents piece
        if board[mid_y][mid_x] == BQ or board[mid_y][mid_x] == BP:
            if board[src_y][src_x] == WP:
                if dst_y ==7:
                    Black_Pieces = Black_Pieces - 1
                    board[src_y][src_x] = EC
                    board[mid_y][mid_x] = EC
                    board[dst_y][dst_x] = WQ
                else:  
                    board[src_y][src_x] = EC
                    board[mid_y][mid_x] = EC
                    board[dst_y][dst_x] = WP
                    Black_Pieces = Black_Pieces
                print_board(board)
                if Black_Pieces == 0:
                    print('White Wins')
                    exit()
            value_package["cur_turn"] = PLAYERS.Black
            print_board(board)
            return jump(value_package, board)

        if src_x == mid_x - 1:
            mid_x = mid_x - 1
            mid_y = mid_y - 1

        
        #cannot jump and empty cell
        if board[mid_y][mid_x] == EC:
            print('No piece to jump over')
            return jump(value_package, board)
           
        mid_x = mid_x +1
        mid_y = mid_y +1

        if board[src_y][src_x] == board[mid_y][mid_x]:
            print('Cannot take your own piece')
            return jump(value_package, board)
        
        if board[src_y][src_x] == WP:
            if dst_y == 7:
                board[src_y][src_x] = EC
                board[dst_y][dst_x] = WQ
            else:
                board[src_y][src_x] = EC
                board[dst_y][dst_x] = WP

        if board[src_y][src_x] == WQ:
            board[src_y][src_x] = EC
            board[dst_y][dst_x] = WQ

        value_package["cur_turn"] = PLAYERS.Black
        print_board(board)
        return jump(value_package, board)

        
main()
