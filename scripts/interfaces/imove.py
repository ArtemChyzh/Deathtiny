from abc import ABC, abstractmethod


class IMove(ABC):
    speed: int

    @abstractmethod
    def move(self):
        raise NotImplementedError
