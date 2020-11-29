import pygame
import string
import keyboard
import time

pygame.init()
pygame.font.init()

string = 'feitoria'

size = 500,300
screen = pygame.display.set_mode(size)

myfont = pygame.font.SysFont('Arial', 35)
black = 0,0,0
number = ''
while True:
    i = 0
    while i <= 7:

        time.sleep(1)

        number = string[i]
        screen.fill((black))
        textsurface = myfont.render(number, False, (255, 255, 255))
        
        screen.blit(textsurface,(0,0))
        pygame.display.flip()

        i += 1

    if keyboard.is_pressed('esc'):
        break

