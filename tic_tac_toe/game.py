from .constants import GRID_SIZE, player
import copy
import random

class TicTacToeGame():
    """
    Represents a tic tac toe game
    """

    def __init__(self):
        # Initialize board
        self.__generate_board()
        # Set turn to player randomly
        self.turn = random.randint(0, 1)
        self.nb_rounds = 0

    # Check if it is a valid move
    def check_move(self, row, column):
        # Out of bound move
        if row >= GRID_SIZE or column >= GRID_SIZE or row < 0 or column < 0:
            return False
        # Square is empty or not
        return self.board[row][column] == "_"
    
    def place(self, row, column):
        # Place symbol on board
        self.board[row][column] = self.turn
        self.nb_rounds += 1

    def __generate_board(self):
        self.board = [ ["_"]*(GRID_SIZE) for _ in range(GRID_SIZE)]

    def change_turn(self):
        if self.turn:
            self.turn = 0
        else:
            self.turn = 1

    # Print board with x and o
    def print_board(self):
        pretty_board = copy.deepcopy(self.board)
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                pretty_board[row][column] = player.get(pretty_board[row][column], " ")
        for row in pretty_board:
            print(row)
    
    def print_current_turn(self):
        # Tell which turn is it
        print("It's", player.get(self.turn), "turn !")

    # Determine if someone has won
    def check_for_win(self):
        return self.__check_row() or self.__check_diagonal() or self.__check_column()

    # The board should be filled after 9 rounds, it's a tie
    def check_for_tie(self):
        return self.nb_rounds == 9

    # Verify if someone has filled a row
    def __check_row(self):
        for row in self.board:
            if self.__check_set(set(row)):
                return True
        return False

    # Verify if someone has filled a diagonal
    def __check_diagonal(self):
        return self.__check_set(set([r[i] for i, r in enumerate(self.board)])) or self.__check_set(set([r[-i-1] for i, r in enumerate(self.board)]))

    # Verify if someone has filled column
    def __check_column(self):
        for column in range(GRID_SIZE):
            if self.__check_set(set([row[column] for row in self.board])):
                return True
        return False

    # Verify it is not empty
    def __check_set(self, set_to_check):
        if len(set_to_check) <= 1:
            if set_to_check.pop() != "_":
                return True
        return False
    