import pygame
from run import runTest
from Controller.keyhandler import KeyHandler
from Utils.handleBuff import HandleBuff
from Utils.handleShield import HandleShield

def handle_events(event, command_box, player, ingame_buff_list, ingame_monster_list,ingame_shield_list):
    if event.type == pygame.KEYDOWN or event.type == pygame.TEXTINPUT:
        command = command_box.handle_input(event)
        if command:
            print("Command entered:", command) 
            if(runTest(command)):
                KeyHandler(command, player)
                HandleBuff(command, ingame_buff_list, ingame_monster_list, player)    
                HandleShield(command,ingame_shield_list)
    return False 