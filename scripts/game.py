import pygame
import settings

pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

if __name__ == "__main__":
    game_over = False
    while not game_over:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()