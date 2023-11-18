from scripts.Base.object import Object


class Item(Object):
    def __init__(self, x: int, y: int, path: str):
        super().__init__(x, y)
        self.image_path: str = path
