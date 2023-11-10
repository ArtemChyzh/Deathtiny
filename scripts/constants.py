from screeninfo import get_monitors
from PIL import Image

monitor = get_monitors()[0]

RELEASE = True
WIDTH = monitor.width if RELEASE else monitor.width/2
HEIGHT = monitor.height if RELEASE else monitor.height/2
FPS = 20

MIN_WIDTH = round(WIDTH / 50) + 1
MAX_WIDTH = MIN_WIDTH * 3
MIN_HEIGHT = round(HEIGHT / 50) + 1
MAX_HEIGHT = MIN_HEIGHT * 3

wall = Image.open('../tiles/room/walls/wall.png')
floor = Image.open('../tiles/room/floor/std_floor.png')
enter = Image.open('../tiles/room/walls/enter.png')
lock = Image.open('../tiles/room/walls/lock_exit.png')
leave = Image.open('../tiles/room/walls/exit.png')
oneway = Image.open('../tiles/room/walls/final_exit.png')
warn = Image.open("../tiles/room/floor/warning_floor.png")
fall = Image.open("../tiles/room/floor/fail_floor.png")

tiles = {
    0: floor,
    1: wall,
    2: enter,
    3: lock,
    4: leave,
    5: oneway,
    6: warn,
    7: fall
}
