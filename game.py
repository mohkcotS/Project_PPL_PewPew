import pygame
from Screen.startScreen import show_start_screen
from Screen.playScreen import show_play_screen


pygame.init()
pygame.display.set_caption("Pew pew")

clock = pygame.time.Clock()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

show_start_screen(screen,width,height,clock)      
show_play_screen(screen,width,height,clock)

pygame.quit()

