from scripts.level import Level
from abc import ABC, abstractmethod


class Square:
    x: int
    y: int
    mode: str

    def __init__(self, x, y, mode):
        self.x = x
        self.y = y
        self.mode = mode


class AbstractLevelFactory(ABC):
    counter: int = 0

    @abstractmethod
    def create(self, is_open=False) -> Level:
        raise NotImplementedError
