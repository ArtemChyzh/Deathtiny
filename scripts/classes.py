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

class Actor(Object):
    speed : int
    damage : int
    health : int

    animation_sheet : dict

    def move() : pass
    def attack() : pass

class Item(Object):
    probability : float
    hidden : bool
    animation_sheet : list

class Tile(Object):
    weight : int
    image_path : str

class Soul(Object): pass

class Hider(Object): pass