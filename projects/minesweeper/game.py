#!/usr/bin/python3

import sys,os
from models import Board, GameState

""" 
    Game loop for the minesweeper game. 
"""

class Game:

    def __init__(self):
        self.board = Board(rows=10, cols=10)

    def play(self):
        self.welcome()
        while self.board.game_state in [GameState.on_going, GameState.start]:
            self.board.print_board_wrapper(self.board.print_board_hook)
            try:
                raw = input("> ")
                line = "".join(raw.split())
                if line[0] == "f":
                    point = tuple(map(int, line[1:].split(",")))
                    self.board.flag_square(point[0], point[1])
                else:
                    point = tuple(map(int, line.split(",")))
                    self.board.click_square(point[0], point[1])
            except (IndexError, ValueError):
                self.help()
            except KeyboardInterrupt:
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
        if self.board.game_state == GameState.lose:
            print("\n\nYou hit a mine. :(\n")
        else:
            print("\n\nYou win!\n")            
        self.board.print_board_wrapper(self.board.print_board_end_hook)

    def welcome(self):
        print("\nWelcome to PySweeper!")
        self.help()
    
    def help(self):
        print("\nEnter coordinates")
        print("> <row>,<column>")
        print("> 1,1")
        print("Flag and unflag coordinates")
        print("> f <row>,<column>")
        print("> f 1,1")

if __name__ == "__main__":
    game = Game()
    game.play()