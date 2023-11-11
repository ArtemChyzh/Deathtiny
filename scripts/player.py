from enum import Enum
from pygame import image


class States(Enum):
    LEFT = 0
    FRONT = 1
    RIGHT = 2
    DOWN = 3


class Player:
    def __init__(self):
        self.speed = 5
        self.x = 70
        self.y = 70

        self.states = ['left', 'top', 'right', 'down']
        self.current_state = states[States.FRONT]

        self.idle = image.load(f"../animation/death/standard/{self.current_state}/idle.png")
        self.move = [
            image.load(f"../animation/death/standard/{self.current_state}/0.png")
            image.load(f"../animation/death/standard/{self.current_state}/1.png")
            image.load(f"../animation/death/standard/{self.current_state}/2.png")
            image.load(f"../animation/death/standard/{self.current_state}/3.png")
        ]
