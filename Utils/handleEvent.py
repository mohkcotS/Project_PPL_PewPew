import pygame
from run import runTest
from Controller.keyhandler import KeyHandler

def handle_events(event, command_box, player):
    if event.type == pygame.KEYDOWN or event.type == pygame.TEXTINPUT:
        command = command_box.handle_input(event)
        if command:
            print("Command entered:", command) 
            if(runTest(command)):
                KeyHandler(command, player)
    return False 