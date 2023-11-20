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
    def no(self): pass
    def crown(self): return CrownState()
    def rage(self): return RageState()


class CrownState(AccessoriesState):
    def __str__(self): return "crown"
    def no(self): pass
    def crown(self): pass
    def rage(self): return FullState()


class RageState(AccessoriesState):
    def __str__(self): return "rage"
    def no(self): pass
    def crown(self): return FullState()
    def rage(self): pass


class FullState(AccessoriesState):
    def __str__(self): return "full"
    def rage(self): pass
    def crown(self): pass
    def no(self): pass
