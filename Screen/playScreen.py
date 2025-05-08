import pygame
from Entity.Player.player import Player
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
from Entity.Monster.leftMonster import LeftMonster
from Entity.Monster.midLeftMonster import MidLeftMonster
from Controller.keyhandler import KeyHandler

def show_play_screen(screen,width,height,clock):
    start_pos = (0, (4/5)*height)
    end_pos = (width, (4/5) *height)
    line_color = (255, 255, 255)
    line_width = 3 

    player = Player()
    monster_right = RightMonster()
    monster_mid_right = MidRightMonster()
    monster_mid = MidMonster()
    monster_left = LeftMonster()
    monster_mid_left = MidLeftMonster()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                KeyHandler(event.key,player)

        screen.fill((0, 0, 0))  # nền đen

        pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)
        player.draw(screen)
        player.update_bullets()
        
        monster_right.draw(screen)
        monster_right.move()
        monster_right.auto_shoot()
        monster_right.update_bullets()
        
        monster_mid_right.draw(screen)
        monster_mid_right.move()
        monster_mid_right.auto_shoot()
        monster_mid_right.update_bullets()
        
        monster_mid.draw(screen)
        monster_mid.move()
        monster_mid.auto_shoot()
        monster_mid.update_bullets()
        
        monster_left.draw(screen)
        monster_left.move()
        monster_left.auto_shoot()
        monster_left.update_bullets()

        monster_mid_left.draw(screen)
        monster_mid_left.move()
        monster_mid_left.auto_shoot()
        monster_mid_left.update_bullets()
        
        pygame.display.flip()
        clock.tick(60)