from enum import Enum


class Weapon(Enum):
    SICKLE = "sickle"
    BLOOD = "blood"
    WAND = "wand"


class Upgrades(Enum):
    NO = "no"
    CROWN = "crown"
    RAGE = "rage"
    FULL = "full"


class Sides(Enum):
    LEFT = "left"
    FRONT = "front"
    RIGHT = "right"
    BACK = "back"


class States(Enum):
    IDLE = "idle"
    MOVE = "move"
    ATTACK = "attack"
    DAMAGE = "damage"
    TP_IN = "tp_in"
    TP_OUT = "tp_out"
