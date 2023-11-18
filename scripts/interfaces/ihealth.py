from abc import ABC, abstractmethod


class IHealth(ABC):
    health: int

    @abstractmethod
    def regenerate(self):
        raise NotImplementedError
