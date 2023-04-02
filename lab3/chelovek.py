import pygame

# инициализация Pygame
pygame.init()

# настройка окна
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Человек')

# цвета
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# нарисовать человека
pygame.draw.circle(screen, blue, (250, 150), 50)  # голова
pygame.draw.line(screen, blue, (250, 200), (250, 350), 4)  # туловище
pygame.draw.line(screen, blue, (250, 250), (200, 300), 4)  # левая рука
pygame.draw.line(screen, blue, (250, 250), (300, 300), 4)  # правая рука
pygame.draw.line(screen, blue, (250, 350), (200, 450), 4)  # левая нога
pygame.draw.line(screen, blue, (250, 350), (300, 450), 4)  # правая нога

# отображение окна
pygame.display.flip()

# ожидание закрытия окна
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# выход из программы
pygame.quit()
