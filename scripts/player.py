from animation import animations
from enumerations import *


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Player(metaclass=Singleton):
    UNIVERSAL_STATES = [States.TP_IN, States.TP_OUT, States.DAMAGE]
    SPEED_SCALE = 10

    def __init__(self):
        self.state: States = States.IDLE
        self.side: Sides = Sides.FRONT
        self.upgrade: Upgrades = Upgrades.NO
        self.weapon: Weapon = Weapon.SICKLE

        self.animation_set: list = animations["death"][f"{States.IDLE.value}"][f"{Weapon.SICKLE.value}"][
            f"{Upgrades.NO.value}"][f"{Sides.FRONT.value}"]

        self.x: int = 200
        self.y: int = 200

        self.max_health: int = 100
        self.health: int = 100
        self.damage: int = 10
        self.speed: int = self.max_health // Player.SPEED_SCALE

    def stop(self): self.state = States.IDLE

    def turn(self, side: Sides):
        self.state = States.IDLE
        self.side = side
        self.set_animation()

    def move(self):
        self.state = States.MOVE
        self.set_animation()
        match self.side:
            case Sides.FRONT: self.y += self.speed
            case Sides.LEFT: self.x -= self.speed
            case Sides.BACK: self.y -= self.speed
            case Sides.RIGHT: self.x += self.speed

    def set_animation(self):
        if self.state in Player.UNIVERSAL_STATES:
            self.animation_set = animations["death"][f"{self.state.value}"]
        else:
            self.animation_set = animations["death"][f"{self.state.value}"][f"{self.weapon.value}"][
                f"{self.upgrade.value}"][f"{self.side.value}"]
