import pygame
import constants

pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), flags=((pygame.NOFRAME)*int(settings.RELEASE)))

player = pygame.image.load("../animation/death/standard/front/idle.png")

if __name__ == "__main__":

    game_over = False
    while not game_over:

        screen.blit(player, (50, 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
