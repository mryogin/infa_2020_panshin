import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

points = 0

def new_ball():
    '''рисует новый шарик '''

    global x,y,r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    global points
    pos_x = max(event.pos[0], x) - min(event.pos[0], x)
    pos_y = max(event.pos[1], y) - min(event.pos[1], y)


    if (pos_x - x) ** 2 + (pos_y - y) ** 2 <= r ** 2:
        points += 1

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    for i in range (randint(1,4)):
        new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

print('Total points:', points)
