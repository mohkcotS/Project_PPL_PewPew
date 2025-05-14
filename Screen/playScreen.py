import pygame
from Entity.Player.player import Player
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
from Entity.Monster.leftMonster import LeftMonster
from Entity.Monster.midLeftMonster import MidLeftMonster
from GameHUD.CommandBox import CommandBox
import random
from Controller.checkCollision import CheckCollision
from Utils.handleEvent import handle_events

def show_play_screen(screen, width, height, clock):
    pygame.key.start_text_input()
    pygame.key.set_text_input_rect(pygame.Rect((width - width//3) // 2, (4/5)*height + 3, width//3, 50))
    
    background = pygame.image.load("src/assets/Space_Background.png")
    background = pygame.transform.scale(background, (width, height))

    line_width = 50

    command_box = CommandBox(screen, width, height, (4/5)*height + line_width)

    player = Player()
    ingame_monster_list = []

    spawn_interval = 3000  
    last_spawn_time = pygame.time.get_ticks() 
    
    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                handle_events(event, command_box, player)

        for monster in ingame_monster_list:
            if (CheckCollision(player, monster)):
                ingame_monster_list.remove(monster)
            if (CheckCollision(monster, player)):
                return    

        if current_time - last_spawn_time >= spawn_interval:
            new_monster = random.choice([MidMonster(),RightMonster(),MidLeftMonster(),MidRightMonster(),LeftMonster()])
            ingame_monster_list.append(new_monster)
            last_spawn_time = current_time


        screen.blit(background, (0, 0))

        # COMMAND BOX
        command_box.draw()

        # PLAYER
        player.draw(screen)
        player.update_bullets()
        
        # MONSTER
        for monster in ingame_monster_list:
            monster.draw(screen)
            monster.move()
            monster.auto_shoot()
            monster.update_bullets()

        pygame.display.flip()
        clock.tick(60)

    pygame.key.stop_text_input()