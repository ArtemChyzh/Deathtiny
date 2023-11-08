class Object():
    x : int
    y : int

    def setPos(self, x, y):
        self.x = x
        self.y = y    
    def modifyPos(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY
    def X(self) : return self.x
    def Y(self) : return self.y
    def checkType() : return "Object"

class Actor(Object):
    speed : int
    damage : int
    health : int

    animation_sheet : dict

    def move() : pass
    def attack() : pass
    def checkType(): return "Actor"

class Item(Object):
    hidden : bool
    def checkType(): return "Item"

class Tile(Object):
    weight : int
    image_path : str

class Soul(Item): pass

class Hider(Actor):
    def __init__(self) -> None:
        self.health = 5
        self.damage = 0
        self.speed = 0