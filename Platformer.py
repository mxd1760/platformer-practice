import pygame
from PlatformerHelper import *

def update(controls,player):
    if controls["left"]:
        player.move_left()
    if controls["right"]:
        player.move_right()
    if controls["up"]:
        player.move_up()
    if controls["down"]:
        player.move_down()
    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Hello World")
    controls = {
        "left": False,
        "right":False,
        "jump":False,
        "up":False,
        "down":False,
    }
    player = Sprite(10,10)
    while True:
        input(controls)
        update(controls,player)
        collisionResolution(player)
        draw(screen,player)

