import pygame
import constants

pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), flags=pygame.NOFRAME if constants.RELEASE else 0)

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
