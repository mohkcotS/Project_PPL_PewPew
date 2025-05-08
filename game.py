import pygame
from Entity.Player.player import Player
from Entity.Bullet.bullet import Bullet
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
from  direction import Direction

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
monster1 = RightMonster()
monster2 = MidRightMonster()
monster3 = MidMonster()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Nhấn Enter để Player bắn
                player.direction = Direction.LEFT_PLAYER
                player.shootBullet(Bullet)
            elif event.key == pygame.K_s:  # Nhấn Enter để Player bắn
                player.direction = Direction.MID_LEFT_PLAYER
                player.shootBullet(Bullet)
            elif event.key == pygame.K_d:  # Nhấn Enter để Player bắn
                player.direction = Direction.MID_PLAYER
                player.shootBullet(Bullet)
            elif event.key == pygame.K_f:  # Nhấn Enter để Player bắn
                player.direction = Direction.MID_RIGHT_PLAYER
                player.shootBullet(Bullet)
            elif event.key == pygame.K_g:  # Nhấn Enter để Player bắn
                player.direction = Direction.RIGHT_PLAYER
                player.shootBullet(Bullet)
            

    screen.fill((0, 0, 0))  # nền đen

    pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)
    player.draw(screen)
    player.update_bullets()
    
    monster1.draw(screen)
    monster1.move()
    monster1.auto_shoot()
    monster1.update_bullets()
    
    monster2.draw(screen)
    monster2.move()
    monster2.auto_shoot()
    monster2.update_bullets()
    
    monster3.draw(screen)
    monster3.move()
    monster3.auto_shoot()
    monster3.update_bullets()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
