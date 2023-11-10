import os
import random
import pygame
import constants
import scenebuilder

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), flags=pygame.NOFRAME if constants.RELEASE else 0)

rooms_count = random.randint(20, 50)
rooms = []
for i in range(rooms_count):
    rooms.append(scenebuilder.RoomMatrix())

actual_room = pygame.image.load(scenebuilder.RoomImage.path_to_room(rooms[0]))
player = pygame.image.load("../animation/death/standard/front/idle.png")
move_right = [
    pygame.image.load("../animation/death/standard/right/0.png"),
    pygame.image.load("../animation/death/standard/right/1.png"),
    pygame.image.load("../animation/death/standard/right/2.png"),
    pygame.image.load("../animation/death/standard/right/3.png")
]

move_left = [
    pygame.image.load("../animation/death/standard/left/0.png"),
    pygame.image.load("../animation/death/standard/left/1.png"),
    pygame.image.load("../animation/death/standard/left/2.png"),
    pygame.image.load("../animation/death/standard/left/3.png")
]

player_anim_count = 0

bg_offset_x = 0
bg_offset_y = 0

if __name__ == "__main__":

    game_over = False
    while not game_over:

        clock.tick(constants.FPS)
        screen.blit(actual_room, (-bg_offset_x, 0))
        screen.blit(move_right[player_anim_count], (70, 70))
        player_anim_count = 0 if player_anim_count == 3 else player_anim_count+1
        bg_offset_x += 10
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
