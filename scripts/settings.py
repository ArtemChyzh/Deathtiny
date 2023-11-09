from screeninfo import get_monitors

monitor = get_monitors()[0]

RELEASE = True
WIDTH = monitor.width if RELEASE else monitor.width/2
HEIGHT = monitor.height if RELEASE else monitor.height/2
FPS = 12
