class Item:
    image_path: str


class Game:
    WIDTH: int
    HEIGHT: int
    FPS: int
    SCENE_COUNT: int

    items_picked = {
    }
    scenes: list


class Scene:
    width: int
    height: int
    enemies: int
    souls: int
