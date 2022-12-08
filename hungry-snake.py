import pygame
from pygame.locals import *
import time

class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1200, 675))
        self.surface.fill((130, 244, 250))
        self.snake = Snake(self.surface)
        self.snake.draw()
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:   # to escape the game
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            self.snake.walk()
            time.sleep(0.2)

class Snake():
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((130, 244, 250))                #refresh the background screen after every movement of snake
        self.parent_screen.blit(self.block, (self.x, self.y))   #place the block at certain coordinates on background screen, surface.blit(source, destination)
        pygame.display.flip()                                   #This will update the contents of the entire display.
        
    def move_left(self):
        self.direction = 'left'
        self.draw()
    def move_up(self):
        self.direction = 'up'
        self.draw()
    def move_right(self):
        self.direction = 'right'
        self.draw()
    def move_down(self):
        self.direction = 'down'
        self.draw()

    def walk(self):
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'right':
            self.x += 10
        if self.direction == 'down':
            self.y += 10
        self.draw()     
        

if __name__ == "__main__":
    game = Game()
    game.run()


    
