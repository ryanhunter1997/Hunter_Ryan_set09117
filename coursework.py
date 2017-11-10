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
    value_package = dict([("board", init_board()), ("turn_count", 1), ("cur_turn", PLAYERS.White)])
    while True:
        print_board(value_package["board"])
        jump(value_package, ["board"])

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
    print("     1 2 3 4 5 6 7 8 \n")
    for i in range (GRID_HEIGHT):
        print(i,  "  |", end="")
        for j in range(GRID_WIDTH):
            print(board[i][j]  + "|", end="")
        print("")
    print("")


def jump(value_package, board):
    src_x = int(input("Choose a x coord to move from "))
    src_y = int(input("Choose a y coord to move from "))
    dst_x = int(input("Choose a y coord to move to "))
    dst_y = int(input("Choose a y coord to move to "))


    x_diff = abs(src_x - dst_X)
    y_diff = abs(src_x - dst_y)

    if sorted([x_diff, y_diff]) != [0, 2]:
        print('invalid coordinates, try again.')
        return

    mid_x = (src_x + dst_x) // 2
    mid_y = (src_y + dst_y) // 2

    if board[src_y][src_x] == '_':
        print('Source cell is empty, try again.')

    if board[dst_y][dst_x] != '_':
        print('Target cell is taken, try again.')

    if board[mid_y][mid_x] == '_':
        print('No piece to jump over')

    if board[src_y][src_x] == board[mid_y][mid_x]:
        print('Cannot take your own piece')

    board[dst_y][dst_x] = board[src_y][src_x]
    board[mid_y][mid_x] = '_'
    board[src_y][src_x] = '_'

main()
