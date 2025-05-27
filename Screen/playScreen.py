import pygame
from Entity.Player.player import Player
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
from Entity.Monster.leftMonster import LeftMonster
from Entity.Monster.midLeftMonster import MidLeftMonster
from Entity.Buffs.buff_Freeze import BuffFreeze
from Entity.Buffs.buff_Lazer import BuffLazer
from Entity.Shield.shield import Shield
from GameHUD.CommandBox import CommandBox
from GameHUD.RulesBox import RulesBox
from GameHUD.StatsBox import StatsBox
from GameHUD.HealthBar import HealthBar
import random
from Controller.checkCollision import CheckCollision
from Utils.handleEvent import handle_events

def show_play_screen(screen, width, height, clock):
    pygame.key.start_text_input()
    pygame.key.set_text_input_rect(pygame.Rect((width - width//3) // 2, (4/5)*height + 3, width//3, 50))
    
    background = pygame.image.load("src/assets/Space_Background.png")
    background = pygame.transform.scale(background, (width, height))

    line_width = 50

    player = Player()

    # Position the health bar
    health_bar_x = player.x - 75  # Center the health bar (150 width / 2)
    health_bar_y = player.y + 90  # Below the player
    health_bar = HealthBar(screen, width, height, health_bar_x, health_bar_y, player)

    command_box = CommandBox(screen, width, height, (4/5)*height + line_width)
    rules_box = RulesBox(screen, width, height, (4/5)*height + line_width - 177, command_box.CHAT_WIDTH)
    stats_box = StatsBox(screen, width, height, (4/5)*height + line_width - 37, command_box.CHAT_WIDTH, player)

    ingame_monster_list = []
    ingame_buff_list = []
    ingame_shield_list = []

    spawn_interval = 8500  
    last_spawn_time = pygame.time.get_ticks() - (spawn_interval - 2000) 
    gameover = False
    


    display_score = 0
    was_gameover = False 
    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                handle_events(event, command_box, player,ingame_buff_list, ingame_monster_list,ingame_shield_list)

        for monster in ingame_monster_list:
            if (CheckCollision(player, monster)):
                monster_x, monster_y = monster.x, monster.y
                direction = monster.direction
                ingame_monster_list.remove(monster)
                player.score += 1
                player.heal_buff += 1
                # if random.random() < 0.3:
                new_buff = random.choice([BuffLazer(monster_x, monster_y, direction), BuffFreeze(monster_x, monster_y, direction)])
                ingame_buff_list.append(new_buff)

            for shield in ingame_shield_list:
                if(CheckCollision(monster,shield)):
                    ingame_shield_list.remove(shield)

            if (CheckCollision(monster, player)):
                gameover = True 


        # Xử lý thu thập buff (Laser và Freeze)
        for buff in ingame_buff_list[:]:
            if CheckCollision(player, buff):
                if isinstance(buff, BuffLazer):
                    player.laser_buff += 1
                elif isinstance(buff, BuffFreeze):
                    player.freeze_buff += 1
                ingame_buff_list.remove(buff)

        if current_time - last_spawn_time >= spawn_interval and random.random() < 0.5 and not gameover:
            new_monster = random.choice([MidMonster(),RightMonster(),MidLeftMonster(),MidRightMonster(),LeftMonster()])
            ingame_monster_list.append(new_monster)
            last_spawn_time = current_time


        screen.blit(background, (0, 0))

        # COMMAND BOX
        command_box.draw()

        # RULES BOX
        rules_box.draw()

        # STATS BOX
        stats_box.draw()

        # Health Bar
        health_bar.draw()

        # BUFF
        for buff in ingame_buff_list[:]: 
            buff.update()
            if isinstance(buff, (BuffLazer, BuffFreeze)) and buff.is_effect and buff.is_expired():
                ingame_buff_list.remove(buff)
            else:
                buff.draw(screen)

        # SHIELD        
        for shield in ingame_shield_list[:]:
            shield.draw(screen)

        if(player.health == 0):
            gameover = True

        # PLAYER
        player.draw(screen)
        if not gameover:
            player.update_bullets()
        
        # MONSTER
        for monster in ingame_monster_list:
            monster.draw(screen)
            if not gameover:
                monster.move()
                monster.auto_shoot()
                monster.update_bullets()

        if gameover and not was_gameover:
            display_score = 0
            was_gameover = True
        elif not gameover:
            was_gameover = False
        
        if gameover:
                if display_score < player.score:
                    display_score += max(1, (player.score // 60))
                    if display_score > player.score:
                        display_score = player.score

        if(gameover == True):
            overlay = pygame.Surface((width, height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))  
            screen.blit(overlay, (0, 0))

            font = pygame.font.Font("src/assets/font/SpaceMonoB.ttf", 28) 
            score_text = font.render("YOUR SCORE: " + str(display_score), True, (255, 255, 255)) 
            game_over = pygame.image.load("src/assets/defeat/game-over.png")
            game_over = pygame.transform.scale(game_over, (600, 400))
            screen.blit(game_over, ((width - game_over.get_width()) // 2, (height - game_over.get_height() - 200) // 2))

            screen.blit(score_text, ((width - score_text.get_width()) // 2, 450))

        pygame.display.flip()
        clock.tick(60)

    pygame.key.stop_text_input()