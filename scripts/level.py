from Base.object import Object
from scripts.settings.leveltiles import TILE_SIZE


class Level:
    def __init__(self, width: int, height: int, enter: Object, leave: Object, matrix: list, img_path: str, locked: bool = True):

        self.width = width
        self.height = height

        self.enter = enter
        self.leave = leave

        self.matrix: list = matrix
        self.locked: bool = locked

        self.img_path = img_path

    def create_bg(self):
        from scripts.settings.leveltiles import tiles
        from PIL import Image

        result = Image.new('RGB', (self.width * TILE_SIZE, self.height * TILE_SIZE), (0, 0, 0))
        for i in self.matrix:
            for j in i:
                result.paste(tiles[j.mode], (j.y*50, j.x*50))
        result.save(self.img_path, "PNG")
