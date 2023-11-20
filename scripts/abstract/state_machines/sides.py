class SideState:
    def left(self): return LeftState()
    def right(self): return RightState()
    def front(self): return FrontState()
    def back(self): return BackState()


class LeftState(SideState):
    def __str__(self): return "left"


class RightState(SideState):
    def __str__(self): return "right"


class FrontState(SideState):
    def __str__(self): return "front"


class BackState(SideState):
    def __str__(self): return "back"
