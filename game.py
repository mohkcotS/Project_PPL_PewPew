import pygame
from Entity.Player.player import Player
from Entity.Bullet.bullet import Bullet
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
from Entity.Monster.leftMonster import LeftMonster
from Entity.Monster.midLeftMonster import MidLeftMonster

pygame.init()
pygame.display.set_caption("Pew pew")

clock = pygame.time.Clock()

width = 800
height = 600

start_pos = (0, (4/5)*height)  # Vị trí bắt đầu (x, y)
end_pos = (width, (4/5) *height)    # Vị trí kết thúc (x, y)
line_color = (255, 255, 255)  # white
line_width = 3 

screen = pygame.display.set_mode((width, height))
        

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
            if event.key == pygame.K_RETURN:  # Nhấn Enter để Player bắn
                player.shootBullet(Bullet)
    

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

pygame.quit()
