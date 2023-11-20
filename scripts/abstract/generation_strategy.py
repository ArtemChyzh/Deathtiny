from abc import ABC, abstractmethod
from scripts.level import Level


class Square:
    x: int
    y: int
    mode: str

    def __init__(self, x, y, mode):
        self.x = x
        self.y = y
        self.mode = mode


class GenerationStrategy(ABC):
    @abstractmethod
    def create(self, is_open=False) -> Level:
        raise NotImplementedError
