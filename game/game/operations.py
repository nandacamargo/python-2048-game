import numpy as np


class Operations:
    def stack(self, game):
        tmp = np.zeros((4, 4), dtype=int)
        for i in range(4):
            position_fill = 0
            for j in range(4):
                if game.matrix[i][j] != 0:
                    tmp[i][position_fill] = game.matrix[i][j]
                    position_fill += 1
        game.matrix = tmp

    def combine(self, game):
        for i in range(4):
            for j in range(3):
                if (
                    game.matrix[i][j] != 0
                    and game.matrix[i][j] == game.matrix[i][j + 1]
                ):
                    game.matrix[i][j] *= 2
                    game.matrix[i][j + 1] = 0
                    game.score += game.matrix[i][j]

    def reverse(self, game):
        game.matrix = np.flip(game.matrix)

    def transpose(self, game):
        game.matrix = np.transpose(game.matrix)
