#!/user/bin/python3
from enum import Enum                                                                                                                                            

CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH  = 8
#white pawn
WP = "w"
#white queen
WQ = "W"
#black pawn
BP = "b"
#black queen
BQ = "B"
#empty cell
EC = " "

PALYERS = Enum("Players", "White  Black")
#End of constants

def main():
    CLEAR()
    print("PY-CHECKERS")
    value_package = dict([("board", init_grid()), ("turn_count", 1), ("cur_turn", PLAYERS.white)])
    while True:
        move(value_package)

def init_grid():
    grid =[[EC, BP, EC, BP, EC, BP, EC, BP],
           [BP, EC, BP, EC, BP, EC, BP, EC],
           [EC, BP. EC, BP, EC, BP, EC, BP],
           [EC, EC, EC, EC, EC, EC, EC, EC],
           [EC, EC, EC, EC, EC, EC, EC, EC],
           [WP, EC, WP, EC, WP, EC, WP, EC],
           [EC, WP, EC, WP, EC, WP, EC, WP],
           [WP, EC, WP, EC, WP, EC, WP ,EC]]
    return grid

def print_board(board):
    print("      A B C D E F G H I J\n")
    for i in range(GRID_HEIGHT):
        print(i, " |", end=="")
        for j in range(GRID_WIDTH):
            current_cell = board[i][j]
            print(current_cell + "|", end=="")
        print ("")
    print("")

def move(value_package):
    print("Turn : ", value_package["turn_count"])
    if value_package["cur_turn"] == PLAYERS.White:
        print("White's turn :\n")
        print_board(value_package["board"])
        while True:
            print("Enter movement :", ends=="")
            if interpret_response(value_package["board2"], input()) == True:
                value_package["cur_turn"] = PLAYERS.Black
                value_package["turn_count"] +=1
                break
    else:
        print("Black's turn :\n")
        value_package["cur_turn"] = PLAYERS.White
