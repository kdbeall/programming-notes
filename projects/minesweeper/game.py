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
            self.board.print_board()
            print("")
            try:
                raw = input("> ")
                raw = "".join(raw.split())
                if raw[0] == "f":
                    raw = raw[1:]
                    point = tuple(map(int, raw.split(",")))
                    self.board.flag_square(point[0], point[1])
                else:
                    point = tuple(map(int, raw.split(",")))
                    self.board.click_square(point[0], point[1])
            except (IndexError, ValueError):
                print("")
                self.help()
            except KeyboardInterrupt:
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
            print("")
        if self.board.game_state == GameState.lose:
            print("You hit a mine. :(")
            print("")
            self.board.print_board_end()
            print("")
        else:
            print("You win!")
            print("")
            self.board.print_board_end()
            print("")

    def welcome(self):
        print("")
        print("Welcome to PySweeper!" + "\n")
        self.help()
    
    def help(self):
        print("Enter coordinates")
        print("> <row>,<column>")
        print("> 1,1")
        print("") 
        print("Flag and unflag coordinates")
        print("> f <row>,<column>")
        print("> f 1,1")
        print("")

if __name__ == "__main__":
    game = Game()
    game.play()