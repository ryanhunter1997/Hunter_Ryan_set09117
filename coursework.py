#!/usr/bin/python3
from enum import Enum


CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8

Black_Pieces = 12
White_Pieces = 12

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
        jump(value_package, board, White_Pieces, Black_Pieces)

def init_board():
    board=[
            ['B', '~', 'w', '~', 'w', '~', 'w', '~'],
            ['~', 'w', '~', '_', '~', 'w', '~', 'w'],
            ['w', '~', 'w', '~', 'b', '~', 'w', '~'],
            ['~', '_', '~', '_', '~', '_', '~', '_'],
            ['_', '~', 'b', '~', '_', '~', '_', '~'],
            ['~', '_', '~', 'b', '~', 'b', '~', 'b'],
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
        
        #exception handling for user inputs
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
        
        #makes sure source coords are within range
        if src_x < 0 or src_x > 7  or src_y < 0 or src_y > 7:
            print("Invalid Source Coord, try again")
            print_board(board)
            return jump(value_package, board, White_Pieces, Black_Pieces)
        
        #makes sure destination coords are within range
        if dst_x < 0 or dst_x > 7  or dst_y < 0 or dst_y > 7:
            print("Destination coord invalid , try again")
            print_board(board)
            return jump(value_package, board, White_Pieces, Black_Pieces)       

        x_diff = abs(src_x - dst_x)
        y_diff = abs(src_x - dst_y)

        mid_x = (src_x + dst_x) // 2
        mid_y = (src_y + dst_y) // 2

    
        #source cell must have a piece in it
        if board[src_y][src_x] == EC:
            print('Source cell is empty, try again.')
            return jump(value_package, board, White_Pieces, Black_Pieces)
        
        #cells out of play
        if board[dst_y][dst_x] == UP:
            print('Unplayable Cell try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)

        #cannot move more than 2 in any direcetion
        if dst_x > src_x + 2 or dst_x < src_x - 2: 
            print('Move is too long, Try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)

        if dst_y > src_y + 2 or dst_y < src_y - 2:
            print ('Move is too long, Try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)
        
        #moves can only be diaginal
        if dst_x == src_x:
            print('You can only move diagonally, try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)
        
        if  dst_y == src_y:
            print('You can only move diagonally, try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)
        
        #cell is taken by piece
        if board[dst_y][dst_x] != EC:
            print('Target cell is taken, try again.')
            return jump(value_package, board, White_Pieces, Black_Pieces)
       
        #cannot move backwards
        if board[src_y][src_x] == BP:
            if dst_y > src_y:
                print("only queens can move backwards")
                return jump(value_package, board, White_Pieces, Black_Pieces)

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
            elif board[src_y][src_x] == BQ:
                board[src_y][src_x] = EC
                board[mid_y][mid_x] = EC
                board[dst_y][dst_x] = BQ
                White_Pieces = White_Pieces -1
            print_board(board)
            if White_Pieces == 0:
                print('Black Wins') #win condition
                exit()    
            #pawn auto taking next piece
            asrc_x = dst_x
            asrc_y = dst_y
            if board[asrc_y][asrc_x] == BP:
                amid_x = asrc_x + 1
                amid_y = asrc_y - 1
                if board[amid_y][amid_x] == WP or board[amid_y][amid_x] == WQ:
                    adst_x = amid_x + 1
                    adst_y = amid_y - 1
                    if board[adst_y][adst_x] == EC:
                        board[asrc_y][asrc_x] = EC
                        board[amid_y][amid_x] = EC
                        board[adst_y][adst_x] = BP
                        White_Pieces = White_Pieces - 1
                if board[asrc_y][asrc_x] == BP:
                    amid_x = asrc_x - 1
                    amid_y = asrc_y - 1
                    if board[amid_y][amid_x] == WP or board[amid_y][amid_x] == WQ:
                        adst_x = amid_x - 1
                        adst_y = amid_y - 1
                        if board[adst_y][adst_x] == EC:
                            board[asrc_y][asrc_x] = EC
                            board[amid_y][amid_x] = EC
                            board[adst_y][adst_x] = BP
                            White_Pieces = White_Pieces - 1
            #king auto taking next piece
            asrc_x = dst_x
            asrc_y = dst_y
            if board[asrc_y][asrc_x] == BQ:
                amid_x = asrc_x + 1
                amid_y = asrc_y - 1
                if board[amid_y][amid_x] == WP or board[amid_y][amid_x] == WQ:
                    adst_x = amid_x + 1
                    adst_y = amid_y - 1
                    if board[adst_y][adst_x] == EC:
                        board[asrc_y][asrc_x] = EC
                        board[amid_y][amid_x] = EC
                        board[adst_y][adst_x] = BQ
                        White_Pieces = White_Pieces - 1
                if board[asrc_y][asrc_x] == BQ:
                    amid_x = asrc_x - 1
                    amid_y = asrc_y - 1
                    if board[amid_y][amid_x] == WP or board[amid_y][amid_x] == WQ:
                        adst_x = amid_x - 1
                        adst_y = amid_y - 1
                        if board[adst_y][adst_x] == EC:
                            board[asrc_y][asrc_x] = EC
                            board[amid_y][amid_x] = EC
                            board[adst_y][adst_x] = BQ
                            White_Pieces = White_Pieces - 1
                if board[asrc_y][asrc_x] == BQ:
                    amid_x = asrc_x + 1
                    amid_y = asrc_y + 1
                if board[amid_y][amid_x] == WP or board[amid_y][amid_x] == WQ:
                    adst_x = amid_x + 1
                    adst_y = amid_y + 1
                    if board[adst_y][adst_x] == EC:
                        board[asrc_y][asrc_x] = EC
                        board[amid_y][amid_x] = EC
                        board[adst_y][adst_x] = BQ
                        White_Pieces = White_Pieces - 1
                if board[asrc_y][asrc_x] == BQ:
                    amid_x = asrc_x - 1
                    amid_y = asrc_y + 1
                    if board[amid_y][amid_x] == WP or board[amid_y][amid_x] == WQ:
                        adst_x = amid_x - 1
                        adst_y = amid_y + 1
                        if board[adst_y][adst_x] == EC:
                            board[asrc_y][asrc_x] = EC
                            board[amid_y][amid_x] = EC
                            board[adst_y][adst_x] = BQ
                            White_Pieces = White_Pieces - 1
            value_package["cur_turn"] = PLAYERS.White
            print_board(board)
            return jump(value_package, board, White_Pieces, Black_Pieces)
        

        if src_x == mid_x + 1:
            mid_x = mid_x + 1
            mid_y = mid_y + 1



        #cannot jump and empty cell
        if board[mid_y][mid_x] == EC:
            print('No piece to jump over')
            return jump(value_package, board, White_Pieces, Black_Pieces)
           
        mid_x = mid_x -1
        mid_y = mid_y -1
      
        #cant take own piece
        if board[src_y][src_x] == board[mid_y][mid_x]:
            print('Cannot take your own piece')
            return jump(value_package, board, White_Pieces, Black_Pieces)
       
        #movement for queen 
        if board[src_y][src_x] == BQ:
            if dst_y < src_y or dst_y > src_y:
                board[dst_y][dst_x] = BQ
                board[src_y][src_x] = EC
                print_board(board)
        
       
       #turns pawn into queen and replaces cells with correct output after move
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
        
        
        #queen taking other pieces  
        if board[src_y][src_x] == BQ:
            if board[mid_y][mid_x] == WP or board[mid_y][mid_x] == WQ:
                if dst_y < src_y or dst_y > src_y:
                    board[mid_y][mid_x] = EC
                    board[src_y][src_x] = EC
                    board[dst_y][dst_x] = BQ
                    print_board(board)
        
        #change whites turn
        value_package["cur_turn"] = PLAYERS.White
        print_board(board)
        return jump(value_package, board, White_Pieces, Black_Pieces)
    
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
            return jump(value_package, board, White_Pieces, Black_Pieces)
        
        if board[dst_y][dst_x] == UP:
            print('Unplayable Cell try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)

        #cannot move more than 2 in any direcetion
        if dst_x > src_x + 2 or dst_x < src_x - 2 :
            print('Move is too long, Try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)

        if dst_y > src_y + 2 or dst_y < src_y - 2 :
            print ('Move is too long, Try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)
        
        #moves can only be diaginal
        if dst_x == src_x:
            print('You can only move diagonally, try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)

        if  dst_y == src_y:
            print('You can only move diagonally, try again')
            return jump(value_package, board, White_Pieces, Black_Pieces)

        if board[dst_y][dst_x] != EC:
            print('Target cell is taken, try again.')
            return jump(value_package, board, White_Pieces, Black_Pieces)

        if board[src_y][src_x] == WP:
            if dst_y < src_y:
                print("only queens can move backwards")
                return jump(value_package, board, White_Pieces, Black_Pieces)


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
            elif board[src_y][src_x] == WQ:
                board[src_y][src_x] = EC
                board[mid_y][mid_x] = EC
                board[dst_y][dst_x] = WQ
                Black_Pieces = Black_Pieces - 1
                print_board(board)
                if Black_Pieces == 0: #win condition
                    print('White Wins')
                    exit()
            #pawn auto taking next piece
            asrc_x = dst_x
            asrc_y = dst_y
            if board[asrc_y][asrc_x] == WP:
                amid_x = asrc_x - 1
                amid_y = asrc_y + 1
                if board[amid_y][amid_x] == BP or board[amid_y][amid_x] == BQ:
                    adst_x = amid_x - 1
                    adst_y = amid_y + 1
                    if board[adst_y][adst_x] == EC:
                        board[asrc_y][asrc_x] = EC
                        board[amid_y][amid_x] = EC
                        board[adst_y][adst_x] = WP
                        White_Pieces = White_Pieces - 1
                if board[asrc_y][asrc_x] == WP:
                    amid_x = asrc_x + 1
                    amid_y = asrc_y + 1
                    if board[amid_y][amid_x] == BP or board[amid_y][amid_x] == BQ:
                        adst_x = amid_x + 1
                        adst_y = amid_y + 1
                        if board[adst_y][adst_x] == EC:
                            board[asrc_y][asrc_x] = EC
                            board[amid_y][amid_x] = EC
                            board[adst_y][adst_x] = WP
                            White_Pieces = White_Pieces - 1
            #king auto taking next piece
            asrc_x = dst_x
            asrc_y = dst_y
            if board[asrc_y][asrc_x] == WQ:
                amid_x = asrc_x + 1
                amid_y = asrc_y - 1
                if board[amid_y][amid_x] == BP or board[amid_y][amid_x] == BQ:
                    adst_x = amid_x + 1
                    adst_y = amid_y - 1
                    if board[adst_y][adst_x] == EC:
                        board[asrc_y][asrc_x] = EC
                        board[amid_y][amid_x] = EC
                        board[adst_y][adst_x] = WQ
                        White_Pieces = White_Pieces - 1
                if board[asrc_y][asrc_x] == WQ:
                    amid_x = asrc_x - 1
                    amid_y = asrc_y - 1
                    if board[amid_y][amid_x] == BP or board[amid_y][amid_x] == BQ:
                        adst_x = amid_x - 1
                        adst_y = amid_y - 1
                        if board[adst_y][adst_x] == EC:
                            board[asrc_y][asrc_x] = EC
                            board[amid_y][amid_x] = EC
                            board[adst_y][adst_x] = WQ
                            White_Pieces = White_Pieces - 1
                if board[asrc_y][asrc_x] == WQ:
                    amid_x = asrc_x + 1
                    amid_y = asrc_y + 1
                if board[amid_y][amid_x] == BP or board[amid_y][amid_x] == BQ:
                    adst_x = amid_x + 1
                    adst_y = amid_y + 1
                    if board[adst_y][adst_x] == EC:
                        board[asrc_y][asrc_x] = EC
                        board[amid_y][amid_x] = EC
                        board[adst_y][adst_x] = WQ
                        White_Pieces = White_Pieces - 1
                if board[asrc_y][asrc_x] == WQ:
                    amid_x = asrc_x - 1
                    amid_y = asrc_y + 1
                    if board[amid_y][amid_x] == BP or board[amid_y][amid_x] == BQ:
                        adst_x = amid_x - 1
                        adst_y = amid_y + 1
                        if board[adst_y][adst_x] == EC:
                            board[asrc_y][asrc_x] = EC
                            board[amid_y][amid_x] = EC
                            board[adst_y][adst_x] = WQ
                            White_Pieces = White_Pieces - 1
            value_package["cur_turn"] = PLAYERS.Black
            print_board(board)
            return jump(value_package, board, White_Pieces, Black_Pieces)

        if src_x == mid_x - 1:
            mid_x = mid_x - 1
            mid_y = mid_y - 1

        
        #cannot jump and empty cell
        if board[mid_y][mid_x] == EC:
            print('No piece to jump over')
            return jump(value_package, board, White_Pieces, Black_Pieces)
           
        mid_x = mid_x +1
        mid_y = mid_y +1

        if board[src_y][src_x] == board[mid_y][mid_x]:
            print('Cannot take your own piece')
            return jump(value_package, board, White_Pieces, Black_Pieces)
       
        #movement for queen 
        if board[src_y][src_x] == WQ:
            if dst_y < src_y or dst_y > src_y:
                board[dst_y][dst_x] = WQ
                board[src_y][src_x] = EC
                print_board(board)
        
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
        return jump(value_package, board, White_Pieces, Black_Pieces)

        
main()
