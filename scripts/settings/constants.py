from screeninfo import get_monitors
from pygame.image import load

monitor = get_monitors()[0]

RELEASE = False
SIZE = {
    "WIDTH": monitor.width if RELEASE else monitor.width // 2,
    "HEIGHT": monitor.height if RELEASE else monitor.height // 2
}
FPS = 8

TITLE = "Deathtiny"
ICON = load("../images/icon.png")

MIN_ROOMS = 20
MAX_ROOMS = 30
