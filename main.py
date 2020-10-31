from tic_tac_toe.game import TicTacToeGame
from tic_tac_toe.constants import GRID_SIZE

def main():
    print("Tic Tac Toe")
    game = TicTacToeGame()
    run = True
    while(run):
        """
        Board :
        [(1,1),(1,2),(1,3)]
        [(2,1),(2,2),(2,3)]
        [(3,1),(3,2),(3,3)]
        """
        game.print_board()
        # Take input as (row,column)
        move = parse(input())
        if move:
            # Valid move
            if game.check_move(move[0],move[1]):
                game.place(move[0],move[1])
            else:
                print("Invalid move")
        else:
            print("Invalid input")
            continue

def parse(input):
    values = input.split(',', 2)
    if len(values) != 2:
        return None
    else:
        types = [int, int]
        try:
            # Cast input as int
            return tuple(type(value)-1 for type, value in zip(types, values))
        except ValueError:
            return None
main()