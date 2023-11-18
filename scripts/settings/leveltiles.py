from PIL import Image
from os.path import dirname, join

current_dir = dirname(__file__)

TILE_SIZE = 50

WALL = Image.open(join(current_dir, '../../tiles/room/walls/wall.png'))
FLOOR = Image.open(join(current_dir, '../../tiles/room/floor/std_floor.png'))
ENTER = Image.open(join(current_dir, '../../tiles/room/walls/enter.png'))
LOCK = Image.open(join(current_dir, '../../tiles/room/walls/lock_exit.png'))
LEAVE = Image.open(join(current_dir, '../../tiles/room/walls/exit.png'))
ONEWAY = Image.open(join(current_dir, '../../tiles/room/walls/final_exit.png'))
WARN = Image.open(join(current_dir, '../../tiles/room/floor/warning_floor.png'))
FALL = Image.open(join(current_dir, '../../tiles/room/floor/fail_floor.png'))

tiles = {
    "floor": FLOOR,
    "wall": WALL,
    "enter": ENTER,
    "lock": LOCK,
    "leave": LEAVE,
    "oneway": ONEWAY,
    "warn": WARN,
    "fall": FALL
}
