import pygame
from system.scene_manager import Scene_Manager

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
manager = Scene_Manager()

while manager.config["RUNNING"]:
    for event in pygame.event.get():
        manager.event_loop(event, pygame)
    screen.fill((0,0,0))

    manager.draw()
        
    manager.update()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()