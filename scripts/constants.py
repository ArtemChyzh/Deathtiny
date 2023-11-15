from screeninfo import get_monitors
from PIL import Image

monitor = get_monitors()[0]

RELEASE = True
WIDTH = monitor.width if RELEASE else monitor.width/2
HEIGHT = monitor.height if RELEASE else monitor.height/2
FPS = 8

MAX_WIDTH = round(WIDTH / 50) + 1
MIN_WIDTH = MAX_WIDTH//2
MAX_HEIGHT = round(HEIGHT / 50) + 1
MIN_HEIGHT = MAX_HEIGHT//2

MIN_ROOMS = 20
MAX_ROOMS = 30

WALL = Image.open('../tiles/room/walls/wall.png')
FLOOR = Image.open('../tiles/room/floor/std_floor.png')
ENTER = Image.open('../tiles/room/walls/enter.png')
LOCK = Image.open('../tiles/room/walls/lock_exit.png')
LEAVE = Image.open('../tiles/room/walls/exit.png')
ONEWAY = Image.open('../tiles/room/walls/final_exit.png')
WARN = Image.open("../tiles/room/floor/warning_floor.png")
FALL = Image.open("../tiles/room/floor/fail_floor.png")

tiles = {
    0: FLOOR,
    1: WALL,
    2: ENTER,
    3: LOCK,
    4: LEAVE,
    5: ONEWAY,
    6: WARN,
    7: FALL
}
