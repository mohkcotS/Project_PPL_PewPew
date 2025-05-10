import pygame
from Entity.Player.player import Player
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
from Entity.Monster.leftMonster import LeftMonster
from Entity.Monster.midLeftMonster import MidLeftMonster
from Controller.keyhandler import KeyHandler
from GameHUD.CommandBox import CommandBox
import random
from Controller.checkCollision import CheckCollision

def handle_events(event, command_box, player):
    """Handle keyboard events for the game."""
    if event.type == pygame.KEYDOWN or event.type == pygame.TEXTINPUT:
        command = command_box.handle_input(event)
        if command:
            print("Command entered:", command)  
            KeyHandler(command, player)
    return False 

def show_play_screen(screen, width, height, clock):
    pygame.key.start_text_input()
    pygame.key.set_text_input_rect(pygame.Rect((width - width//3) // 2, (4/5)*height + 3, width//3, 50))
    
    background = pygame.image.load("src/assets/Space_Background.png")
    background = pygame.transform.scale(background, (width, height))

    start_pos = (0, (4/5)*height)
    end_pos = (width, (4/5) *height)
    line_color = (255, 255, 255)
    line_width = 50

    command_box = CommandBox(screen, width, height, (4/5)*height + line_width)

    player = Player()
    ingame_monster_list = []

    # Biến thời gian
    spawn_interval = 3000  # 3 giây = 3000 milliseconds
    last_spawn_time = pygame.time.get_ticks()  # thời điểm spawn gần nhất
    
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
                print("Player bullet hit by monster!")
                ingame_monster_list.remove(monster)
            if (CheckCollision(monster, player)):
                return    

        if current_time - last_spawn_time >= spawn_interval:
            # MidMonster(),RightMonster(),,MidLeftMonster()MidRightMonster(),
            new_monster = random.choice([MidMonster(),RightMonster(),MidLeftMonster(),MidRightMonster(),LeftMonster()])
            ingame_monster_list.append(new_monster)
            last_spawn_time = current_time

        # BACKGROUND
        screen.blit(background, (0, 0))
        # pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)

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