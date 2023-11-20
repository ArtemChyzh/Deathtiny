from abc import ABC, abstractmethod


class SideState(ABC):
    @abstractmethod
    def left(self): raise NotImplementedError
    @abstractmethod
    def right(self): raise NotImplementedError
    @abstractmethod
    def front(self): raise NotImplementedError
    @abstractmethod
    def back(self): raise NotImplementedError


class LeftState(SideState):
    def __str__(self): return "left"
    def left(self): pass
    def right(self): return RightState()
    def front(self): return FrontState()
    def back(self): return BackState()


class RightState(SideState):
    def __str__(self): return "right"
    def left(self): return LeftState()
    def right(self): pass
    def front(self): return FrontState()
    def back(self): return BackState()


class FrontState(SideState):
    def __str__(self): return "front"
    def left(self): return LeftState()
    def right(self): return RightState()
    def front(self): pass
    def back(self): return BackState()


class BackState(SideState):
    def __str__(self): return "back"
    def left(self): return LeftState()
    def right(self): return RightState()
    def front(self): return FrontState()
    def back(self): pass
