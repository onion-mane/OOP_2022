import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


# rect(screen, (255, 0, 255), (100, 100, 200, 200))

# polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               # (300,100), (100,100)])
# polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               # (300,100), (100,100)], 5)


circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 255, 255), (200, 175), 100, 5)


circle(screen, (255, 0, 0), (150, 150), 25)
circle(screen, (0, 0, 0), (150, 150), 25, 5)
circle(screen, (0, 0, 0), (150, 150), 10)

circle(screen, (255, 0, 0), (250, 150), 20)
circle(screen, (0, 0, 0), (250, 150), 20, 5)
circle(screen, (0, 0, 0), (250, 150), 8)

rect(screen, (0, 0, 0), (150, 200, 100, 30))

#polygon(screen, (0, 0, 0), [(150, 150), (150, 140), (175, 125), (175, 115)])
line(screen, (100, 100, 100), (100, 85), (200, 125), 20)
line(screen, (100, 100, 100), (300, 85), (220, 125), 20)
pygame.display.update()


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
