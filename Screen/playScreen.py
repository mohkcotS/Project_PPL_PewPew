import pygame
from Entity.Player.player import Player
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
from Entity.Monster.leftMonster import LeftMonster
from Entity.Monster.midLeftMonster import MidLeftMonster
from Entity.Buffs.buff_Freeze import BuffFreeze
from Entity.Buffs.buff_Lazer import BuffLazer
from GameHUD.CommandBox import CommandBox
from GameHUD.RulesBox import RulesBox
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
    rules_box = RulesBox(screen, width, height, (4/5)*height + line_width - 177, command_box.CHAT_WIDTH)

    player = Player()
    ingame_monster_list = []
    ingame_buff_list = []

    spawn_interval = 7000  
    last_spawn_time = pygame.time.get_ticks() - (spawn_interval - 2000) 
    
    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                handle_events(event, command_box, player,ingame_buff_list, ingame_monster_list)

        for monster in ingame_monster_list:
            if (CheckCollision(player, monster)):
                monster_x, monster_y = monster.x, monster.y
                direction = monster.direction
                ingame_monster_list.remove(monster)
                player.heal_buff += 1
                print(player.heal_buff)
                # if random.random() < 0.3:
                new_buff = random.choice([BuffLazer(monster_x, monster_y, direction), BuffFreeze(monster_x, monster_y, direction)])
                ingame_buff_list.append(new_buff)
            # if (CheckCollision(monster, player)):
                # return    

        if current_time - last_spawn_time >= spawn_interval and random.random() < 0.5:
            new_monster = random.choice([MidMonster(),RightMonster(),MidLeftMonster(),MidRightMonster(),LeftMonster()])
            ingame_monster_list.append(new_monster)
            last_spawn_time = current_time


        screen.blit(background, (0, 0))

        # COMMAND BOX
        command_box.draw()

        # RULES BOX
        rules_box.draw()

        #BUFF
        for buff in ingame_buff_list[:]: 
            buff.update()
            if isinstance(buff, (BuffLazer, BuffFreeze)) and buff.is_effect and buff.is_expired():
                ingame_buff_list.remove(buff)
            else:
                buff.draw(screen)

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