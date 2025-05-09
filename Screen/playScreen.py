import pygame
from Entity.Player.player import Player
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
from Entity.Monster.leftMonster import LeftMonster
from Entity.Monster.midLeftMonster import MidLeftMonster
from Controller.keyhandler import KeyHandler
import random

def show_play_screen(screen,width,height,clock):
    start_pos = (0, (4/5)*height)
    end_pos = (width, (4/5) *height)
    line_color = (255, 255, 255)
    line_width = 3 

    player = Player()
    ingame_monster_list = []

    # Biến thời gian
    spawn_interval = 3000  # 3 giây = 3000 milliseconds
    last_spawn_time = pygame.time.get_ticks()  # thời điểm spawn gần nhất
    
    running = True
    while running:
        current_time = pygame.time.get_ticks()

        if current_time - last_spawn_time >= spawn_interval:
            new_monster = random.choice([RightMonster(),MidRightMonster(),MidMonster(),LeftMonster(),MidLeftMonster()])
            ingame_monster_list.append(new_monster)
            last_spawn_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                KeyHandler(event.key,player)

        screen.fill((0, 0, 0))  # nền đen

        pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)
        player.draw(screen)
        player.update_bullets()
        
        for monster in ingame_monster_list:
            monster.draw(screen)
            monster.move()
            monster.auto_shoot()
            monster.update_bullets()
        
        pygame.display.flip()
        clock.tick(60)