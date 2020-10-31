from .constants import GRID_SIZE, player
import copy

class TicTacToeGame():
    """
    TicTacToe class
    """

    def __init__(self):
        self.board = self.init_board()
        # Set start turn to player "x"
        self.turn = 0

    def check_move(self, row, column):
        # Out of bound move
        if row >= GRID_SIZE or column >= GRID_SIZE or row < 0 or column < 0:
            print("Out of bound")
            return False
        # Square is already filled
        if self.board[row][column] != "_":
            print("Already filled")
            return False
        print("All good")
        return True
    
    def place(self, row, column):
        self.board[row][column] = self.turn
        self.change_turn()

    def init_board(self):
        board = [ ["_"]*(GRID_SIZE) for i in range(GRID_SIZE)]
        return board
    
    def change_turn(self):
        if self.turn:
            self.turn = 0
        else:
            self.turn = 1

    def print_board(self):
        pretty_board = copy.deepcopy(self.board)
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                pretty_board[row][column] = player.get(pretty_board[row][column], " ")

        for row in pretty_board:
            print(row)

    def winner(self):
        pass