from scripts.enemy import Enemy
from abc import ABC, abstractmethod


class AbstractEnemyFactory(ABC):
    @abstractmethod
    def create(self) -> Enemy:
        raise NotImplementedError
