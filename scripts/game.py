import os
import random
import pygame
import animation
import constants

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), flags=pygame.NOFRAME if constants.RELEASE else 0)

rooms_count = random.randint(20, 50)
rooms = []

anim_set: dict = animation.animations["death"]["sickle"]["no"]
move_right: list = anim_set["right"]["move"]
move_left: list = anim_set["left"]["move"]
attack_right: list = anim_set["right"]["attack"]

player_anim_count: int = 0

if __name__ == "__main__":

    game_over = False
    while not game_over:

        clock.tick(constants.FPS)
        screen.blit(move_right[player_anim_count], (70, 70))
        player_anim_count = 0 if player_anim_count == len(move_right)-1 else player_anim_count+1
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                for filename in os.listdir("../rooms"):
                    file_path = os.path.join("../rooms", filename)
                    try:
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                    except Exception as e:
                        print(f"Error while deleting file {file_path}. {e}")
                pygame.quit()
