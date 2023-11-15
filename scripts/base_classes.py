from enumerations import States


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Object:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y

    def modify_position(self, delta_x=0, delta_y=0):
        self.x += delta_x
        self.y += delta_y


class Item(Object):
    def __init__(self, x: int, y: int, path: str):
        super().__init__(x, y)
        self.image_path: str = path


class Actor(Object):
    def __init__(self, x: int = 0, y: int = 0):
        super().__init__(x, y)

        self.power: int
        self.health: int
        self.speed: int

        self.state: States = States.IDLE

        self.animation_set: dict
        self.animation_pointer: int = 0

    def move(self):
        raise NotImplementedError()

    def attack(self):
        raise NotImplementedError()
