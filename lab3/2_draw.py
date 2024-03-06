import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 400))
screen.fill((255, 255, 255))



####################
circle(screen, (255, 102, 0), (200, 400), 100)

ellipse(screen, (0, 0, 139), (100, 80, 200, 200))
ellipse(screen, (233, 198, 175), (100, 100, 200, 250))

ellipse(screen, (233, 198, 175), (50, 30, 35, 40))
ellipse(screen, (233, 198, 175), (305, 30, 35, 40))
####################

####################
circle(screen, (0, 200, 64), (600, 400), 100)

ellipse(screen, (160, 128, 96), (500, 80, 200, 200))
ellipse(screen, (233, 198, 175), (500, 100, 200, 250))

ellipse(screen, (233, 198, 175), (450, 30, 35, 40))
ellipse(screen, (233, 198, 175), (705, 30, 35, 40))
####################



rect(screen, (0, 255, 0), (0, 0, 800, 50))  #квадрат
rect(screen, (0, 0, 0), (0, 0, 800, 50), 2)  #обводка

#############
line(screen, (233, 198, 175), (65,50),(75,300),20)
line(screen, (233, 198, 175), (320,300),(320,50),20)
polygon(screen, (255, 102, 0), [(60, 300),
                                            (110, 275),
                                            (150, 300),
                                            (120, 350),
                                            (75, 340)])

polygon(screen, (255, 102, 0), [(340, 300),
                                            (290, 275),
                                            (250, 300),
                                            (280, 350),
                                            (325, 340)])

polygon(screen, (255, 0, 0), [(140, 260),
                                            (200, 295),
                                            (260, 260)])
circle(screen, (210, 105, 30), (200, 240), 10)


circle(screen, (188, 143, 143), (250, 220), 20)
circle(screen, (188, 143, 143), (150, 220), 20)
circle(screen, (0, 0, 0), (250, 220), 7)
circle(screen, (0, 0, 0), (150, 220), 7)
###########################

###########################
line(screen, (233, 198, 175), (465,50),(475,300),20)
line(screen, (233, 198, 175), (720,300),(720,50),20)
polygon(screen, (0, 200, 64), [(460, 300),
                                            (510, 275),
                                            (550, 300),
                                            (520, 350),
                                            (475, 340)])

polygon(screen, (0, 200, 64), [(740, 300),
                                            (690, 275),
                                            (650, 300),
                                            (680, 350),
                                            (725, 340)])

polygon(screen, (255, 0, 0), [(540, 260),
                                            (600, 295),
                                            (660, 260)])
circle(screen, (210, 105, 30), (600, 240), 10)


circle(screen, (80, 208, 255), (650, 220), 20)
circle(screen, (80, 208, 255), (550, 220), 20)
circle(screen, (0, 0, 0), (650, 220), 7)
circle(screen, (0, 0, 0), (550, 220), 7)
###########################
f1 = pygame.font.SysFont('arial', 40)
text1 = f1.render('PYTHON is REALLY AMAZING', True, (0, 0, 0))
screen.blit(text1, (180, 0))
pygame.display.update()


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()