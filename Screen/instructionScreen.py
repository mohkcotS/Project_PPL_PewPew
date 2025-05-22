import pygame
from Screen.dirInsScreen import show_direction_screen
from Screen.buffInsScreen import show_buff_screen
from Screen.syntaxInsScreen import show_syntax_screen

def show_instruction_screen(screen, width, height, clock):
    show_direction_screen(screen, width, height, clock)
    show_buff_screen(screen, width, height, clock)
    show_syntax_screen(screen, width, height, clock)

pygame.quit()