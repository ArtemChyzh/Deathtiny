class Object:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y

    def modify_position(self, delta_x=0, delta_y=0):
        self.x += delta_x
        self.y += delta_y
