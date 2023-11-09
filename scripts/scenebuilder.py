from constants import *
from random import randint
from PIL import Image


class Tablet:
    x: int
    y: int
    mode: int

    def __init__(self, x, y, mode):
        self.x = x
        self.y = y
        self.mode = mode


class RoomMatrix:
    counter = 0

    def __init__(self):

        self.counter = RoomMatrix.counter
        self.width = randint(MIN_WIDTH, MAX_WIDTH)
        self.height = randint(MIN_HEIGHT, MAX_HEIGHT)

        exit_y = randint(3, self.height - 3)

        self.matrix = []

        for i in range(self.height):
            line = []
            for j in range(self.width):
                if j == 0 and i == 5:
                    line.append(Tablet(j, i, 2))
                elif j == self.width - 1 and i == exit_y:
                    line.append(Tablet(j, i, 3))
                elif i in (0, self.height - 1) or j in (0, self.width - 1):
                    line.append(Tablet(j, i, 1))
                else:
                    line.append(Tablet(j, i, 0))
            self.matrix.append(line)

        RoomMatrix.counter += 1


class RoomImage:
    @staticmethod
    def draw(matrix: RoomMatrix):
        result = Image.new('RGB', (matrix.width * 50, matrix.height * 50), (0, 0, 0))
        for i in matrix.matrix:
            for j in i:
                result.paste(tiles[j.mode], (j.x * 50, j.y * 50))
        result.save(f"../rooms/{matrix.counter}.png", "PNG")
