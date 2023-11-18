import pygame
from scripts.settings import constants
from scripts.LevelFactories.simple_level_factory import SimpleLevel

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((constants.SIZE["WIDTH"], constants.SIZE["HEIGHT"]),
                                 flags=pygame.NOFRAME if constants.RELEASE else 0)
pygame.display.set_caption(constants.TITLE)
pygame.display.set_icon(constants.ICON)

levels = []
current_level = 0

levels.append(SimpleLevel().create())
levels[current_level].create_bg()
bg = pygame.image.load(levels[current_level].img_path)


if __name__ == "__main__":
    game_over = False
    while not game_over:
        clock.tick(constants.FPS)

        pygame.display.update()
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
