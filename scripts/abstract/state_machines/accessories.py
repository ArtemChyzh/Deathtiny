from abc import ABC, abstractmethod


class AccessoriesState(ABC):
    @abstractmethod
    def no(self): raise NotImplementedError
    @abstractmethod
    def crown(self): raise NotImplementedError
    @abstractmethod
    def rage(self): raise NotImplementedError


class NoAccessoryState(AccessoriesState):
    def __str__(self): return "no"
    def no(self): return NoAccessoryState()
    def crown(self): return CrownState()
    def rage(self): return RageState()


class CrownState(AccessoriesState):
    def __str__(self): return "crown"
    def no(self): return CrownState()
    def crown(self): return CrownState()
    def rage(self): return FullState()


class RageState(AccessoriesState):
    def __str__(self): return "rage"
    def no(self): return RageState()
    def crown(self): return FullState()
    def rage(self): return RageState()


class FullState(AccessoriesState):
    def __str__(self): return "full"
    def rage(self): return FullState()
    def crown(self): return FullState()
    def no(self): return FullState()
