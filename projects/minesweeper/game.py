#!/usr/bin/python3

from models import Board, GameState
""" Game loop for the minesweeper game. """

class Game:

    def __init__(self):
        self.board = Board(rows=10, cols=10)

    def play(self):
        self.welcome()
        while self.board.game_state in [GameState.on_going, GameState.start]:
            self.board.print_board()
            print("")
            try:
                point = tuple(map(int, input("> ").split(",")))
                self.board.click_square(point[0], point[1])
            except Exception:
                print("")
                self.help()
            print("")
        if self.board.game_state == GameState.lose:
            print("You hit a mine. :(")
            print("")

    def welcome(self):
        print("")
        print("Welcome to PySweeper!" + "\n")
        self.help()
    
    def help(self):
        print("Enter coordinates like this.")
        print("> <row>,<column>")
        print("For example,")
        print("> 1,1")
        print("")        

if __name__ == "__main__":
    game = Game()
    game.play()