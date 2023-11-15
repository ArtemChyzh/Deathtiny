from animation import animations
from enumerations import *
from base_classes import Actor, Singleton, Item


class Player(Actor, metaclass=Singleton):
    UNIVERSAL_STATES = [States.TP_IN, States.TP_OUT, States.DAMAGE]
    SPEED_SCALE = 10

    def __init__(self, x: int = 200, y: int = 200):
        super().__init__(x, y)

        self.x: int = x
        self.y: int = y

        self.inventory: list = []

        self.max_health: int = 100
        self.speed: int = self.max_health // Player.SPEED_SCALE
        self.health: int = self.max_health
        self.damage: int = 10

        self.weapon: Weapon = Weapon.SICKLE
        self.upgrade: Upgrades = Upgrades.NO
        self.side: Sides = Sides.FRONT
        self.state: States = States.IDLE

        self.animation_config: dict = animations["death"][f"{self.weapon.value}"][f"{self.upgrade.value}"]
        self.animation_set = self.animation_config[f"{self.side.value}"][f"{self.state.value}"]

    def update_animation(self):
        if self.state in Player.UNIVERSAL_STATES:
            self.animation_set = animations["death"][f"{self.state.value}"]
        else:
            self.animation_set = self.animation_config[f"{self.side.value}"][f"{self.state.value}"]

    def stop(self):
        self.state = States.IDLE
        self.update_animation()

    def turn(self, side: Sides):
        self.state = States.IDLE
        self.side = side
        self.update_animation()

    def move(self):
        self.state = States.MOVE
        self.update_animation()
        match self.side:
            case Sides.FRONT: self.modify_position(delta_y=self.speed)
            case Sides.LEFT: self.modify_position(delta_x=-self.speed)
            case Sides.BACK: self.modify_position(delta_y=-self.speed)
            case Sides.RIGHT: self.modify_position(delta_x=self.speed)

    def teleport(self, x: int, y: int):
        self.state = States.TP_OUT
        self.update_animation()
        self.set_position(x, y)
        self.state = States.TP_IN
        self.update_animation()

    def pick_up(self, item: Item):
        self.inventory.append(item)
