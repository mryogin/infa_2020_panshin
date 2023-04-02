import pygame
from pygame.draw import *
from pygame.color import THECOLORS

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

yellow = THECOLORS['yellow']
red = THECOLORS['red']
black = THECOLORS['black']

#face
circle(screen, yellow, (200,200), 200)

#eye
def eye(pos:tuple, rad):
    small_radius = rad // 4
    circle(screen, red, pos, rad)
    circle(screen, black, pos, (small_radius) )

#left_eye
eye((100,150), 40)
#right_eye
eye((300,150), 30)

#mouth
rect(screen, black, (125, 300, 150,20))

#left eyebrow
xy1 = (50,150)
xy2 = (55,155)
xy3 = (150,50)
xy4 = (155,55)
polygon(screen, black,[(25,150), (35,155), (135,55), (130,45)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()