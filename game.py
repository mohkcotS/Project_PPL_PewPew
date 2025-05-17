import pygame
import subprocess
from Screen.startScreen import show_start_screen
from Screen.playScreen import show_play_screen

import sys
subprocess.run([sys.executable, "run.py", "gen"])

pygame.init()
pygame.display.set_caption("Pew pew")

clock = pygame.time.Clock()
width = 1200
height = 800
screen = pygame.display.set_mode((width, height))

show_start_screen(screen,width,height,clock)      
show_play_screen(screen,width,height,clock)

pygame.quit()