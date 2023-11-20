from scripts.abstract.generation_strategy import GenerationStrategy, Square
from scripts.settings.leveltiles import TILE_SIZE
from scripts.settings.constants import SIZE
from scripts.level import Level


class FinalLevelStrategy(GenerationStrategy):
    def create(self, is_open=False) -> Level:
        width: int = SIZE["WIDTH"] // TILE_SIZE
        height: int = SIZE["HEIGHT"] // TILE_SIZE
        enter = None
        leave = None

        matrix = []
        for i in range(height):
            line = []
            for j in range(width):
                mode: str
                if i in (0, height - 1) or j in (0, width - 1):
                    mode = "wall"
                else:
                    mode = "floor"
                line.append(Square(i, j, mode))
            matrix.append(line)

        level: Level = Level(width=width, height=height, enter=enter, leave=leave, matrix=matrix)
        return level
