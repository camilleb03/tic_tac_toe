from tic_tac_toe.game import TicTacToeGame
from tic_tac_toe.constants import GRID_SIZE, player

import sys

def main():
    print("Tic Tac Toe")
    playing = False
    show_actions_menu()
    while(True):
        # Take input from user
        action = input()

        # Verify if user wants to quit
        if str(action).lower() == "q":
            # Quit game
            print("Thanks for playing!")
            sys.exit()

        # Show actions menu
        if str(action).lower() == "a":
            show_actions_menu()
            continue

        # Show help menu
        if str(action).lower() == "h":
            show_help_menu()
            continue

        # Start a game
        if str(action).lower()== "p":
            game = TicTacToeGame()
            playing = True
            game.print_board()
        # Not a valid input
        else:
            show_wrong_input()

        """
        Board :
        [(1,1),(1,2),(1,3)]
        [(2,1),(2,2),(2,3)]
        [(3,1),(3,2),(3,3)]
        """
        while(playing):
            # Take input as (row,column)
            move = parse(input())
            if move:
                # Valiate move (not out of bounds or already filled)
                if game.check_move(move[0],move[1]):
                    game.place(move[0],move[1])
                    game.print_board()
                    if game.check_for_win():
                        print(player.get(game.turn), "has won !")
                        playing = False
                        show_actions_menu()
                    
                    elif game.check_for_tie():
                        print("It's a tie")
                        playing = False
                        show_actions_menu()
                else:
                    print("Invalid move")
        

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

def show_actions_menu():
    print("---- POSSIBLE ACTIONS ----")
    print("p - Start a game")
    print("h - Help")
    print("q - Quit game")
    print("--------------------------")

def show_help_menu():
    print("------ HOW IT WORKS ------")
    print("Input row,column to play")
    print("i.e. 1,2 :")
    print("    1   2   3  ")
    print("1 [' ','x',' ']")
    print("2 [' ',' ',' ']")
    print("3 [' ',' ',' ']")
    print("--------------------------")

def show_wrong_input():
    print("Wrong action!")
    show_actions_menu()

main()