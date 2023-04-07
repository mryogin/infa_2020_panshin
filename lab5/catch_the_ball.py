import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 1
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
    """
    Функция рисует новый шарик случайного радиуса и цвета в случайном месте на экране
    """
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    """
    Функция обрабатывает клик пользователя и увеличивает количество очков при попадании в шарик
    """
    global points
    pos_x = event.pos[0]
    pos_y = event.pos[1]

    if (pos_x - x) ** 2 + (pos_y - y) ** 2 <= r ** 2:
        points += 1
        print(points)


def update_display():
    """
    Функция обновляет экран
    """
    pygame.display.update()

def fill_screen():
    """
    Функция заполняет экран черным цветом
    """
    screen.fill(BLACK)

def run_game():
    """
    Функция запускает основной цикл игры
    """
    global finished, clock
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)

        for i in range(randint(1, 4)):
            new_ball()

        update_display()
        fill_screen()

    pygame.quit()

if __name__ == '__main__':
    run_game()
    print('Total points:', points)
