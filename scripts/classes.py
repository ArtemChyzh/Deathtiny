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

class Room():
    scene : list = [[]]

    boss_fight : bool
    item_list : list
    enemy_list : list
    
    def create() : pass

class Game():
    war_room_list : list
    starve_room_list : list
    plague_room_list : list


class Gamer(Actor):
    def __init__(self) -> None:
        self.speed = 10
        self.damage = 1
        self.health = 10

        self.animation_sheet : dict
        self.inventory : set = ()

class Floor(Tile):
    def __init__(self) -> None:
        self.weight = 0
        self.image_path = ""

class Wall(Tile):
    def __init__(self) -> None:
        self.weight = 100
        self.image_path = ""