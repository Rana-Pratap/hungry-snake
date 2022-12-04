import pygame
from pygame.locals import *
# import time

def draw_block():
    surface.fill((130, 244, 250))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    # set the size of game window
    surface = pygame.display.set_mode((1200, 675))

    # pick color of our choise to fill game window from black
    surface.fill((130, 244, 250))

    block = pygame.image.load("resources/block.jpg").convert()
    block_x = 50
    block_y = 50
    surface.blit(block,(block_x, block_y))

    # this will change black to our color of choice
    pygame.display.flip()


    running =True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
            elif event.type == QUIT:
                running = False


    # to keep the window for certain amount of time
    # time.sleep(10)
 