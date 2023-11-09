from screeninfo import get_monitors

monitor = get_monitors()[0]
WIDTH = monitor.width/2
HEIGHT = monitor.height/2
FPS = 8