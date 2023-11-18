from abc import ABC, abstractmethod


class IAttack(ABC):
    power: int

    @abstractmethod
    def attack(self):
        raise NotImplementedError
