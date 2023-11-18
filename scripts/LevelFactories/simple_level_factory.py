from scripts.abstract.level_factory import AbstractLevelFactory, Square
from scripts.settings.leveltiles import TILE_SIZE
from scripts.settings.constants import SIZE
from scripts.Base.object import Object
from scripts.level import Level
from random import randint, choice


class SimpleLevel(AbstractLevelFactory):
    def create(self, is_open=False) -> Level:
        width: int = SIZE["WIDTH"] // TILE_SIZE
        height: int = SIZE["HEIGHT"] // TILE_SIZE
        enter: Object = Object(0, 5)
        if choice((True, False)):
            location: int = randint(3, height - 3)
            leave: Object = Object(width - 1, location)
        else:
            location: int = randint(3, width - 3)
            leave: Object = Object(location, choice([height - 1, 0]))
        matrix = []

        for i in range(height):
            line = []
            for j in range(width):
                mode: str
                if j == 0 and i == 5:
                    mode = "enter"
                elif j == leave.x and i == leave.y:
                    mode = "leave" if is_open else "lock"
                elif i in (0, height - 1) or j in (0, width - 1):
                    mode = "wall"
                else:
                    mode = "floor"
                line.append(Square(i, j, mode))
            matrix.append(line)

        level: Level = Level(width=width, height=height, enter=enter, leave=leave, matrix=matrix, img_path=f"../rooms/{AbstractLevelFactory.counter}.png")

        AbstractLevelFactory.counter += 1
        return level
