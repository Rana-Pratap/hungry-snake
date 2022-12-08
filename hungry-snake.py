import pygame
from pygame.locals import *
import time

SIZE = 40

class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1200, 675))
        self.surface.fill((130, 244, 250))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        # self.apple = Apple(self.surface)
        # self.apple.draw()
    
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
            self.snake.walk()                                   # if any direction key is not pressed it will continue to move in one direction
            time.sleep(0.2)                                     # after how second to move next automatically

class Snake():
    def __init__(self, parent_screen, length):

        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((130, 244, 250))                #refresh the background screen after every movement of snake
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))   
                                                                #place the block at certain coordinates on background screen, surface.blit(source, destination)
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

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()        

# class Apple():
#     def __init__(self, parent_screen):
#         self.parent_screen = parent_screen
#         self.apple = pygame.image.load("resources/apple.jpg").convert()
#         self.x = SIZE*3
#         self.y = SIZE*3
    
#     def draw(self):
#         self.parent_screen.blit(self.block, (self.x, self.y))
#         pygame.display.flip() 

if __name__ == "__main__":
    game = Game()
    game.run()


    
