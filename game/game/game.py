import random
import tkinter as tk

import numpy as np

import gui as G
import operations as o

gui = G.GUI()
operations = o.Operations()


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 Game")

        self.start_game()

    def start_game(self):
        # Matrix 4X4 filled with zeros
        self.matrix = np.zeros((4, 4), dtype=int)

        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.score = 0

    # Adds 2 or 4 tile to an empty cell at random
    def add_tile(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while self.matrix[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

    # Check if game is over
    def end_game(self):
        if any(2048 in row for row in self.matrix):
            gui.message("YOU WIN!", 1)
        elif (
            not any(0 in row for row in self.matrix)
            and not self.exists_horizontal_moves()
            and not self.exists_vertical_moves()
        ):
            gui.message("GAME OVER!", 0)

    def exists_horizontal_moves(
        self,
    ):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    def exists_vertical_moves(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False


def main():
    Game()


if __name__ == "__main__":
    main()
