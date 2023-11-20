from abc import ABC, abstractmethod


class WeaponState(ABC):
    @abstractmethod
    def sickle(self): raise NotImplementedError
    @abstractmethod
    def blood_sickle(self): raise NotImplementedError
    @abstractmethod
    def wand(self): raise NotImplementedError


class SickleState(WeaponState):
    def __str__(self): return "sickle"
    def sickle(self): return SickleState()
    def blood_sickle(self): return BloodState()
    def wand(self): return WandState()


class BloodState(WeaponState):
    def __str__(self): return "blood"
    def sickle(self): return BloodState()
    def blood_sickle(self): return BloodState()
    def wand(self): return WandState()


class WandState(WeaponState):
    def __str__(self): return "wand"
    def sickle(self): return WandState()
    def blood_sickle(self): return BloodState()
    def wand(self): return WandState()
