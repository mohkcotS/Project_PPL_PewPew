import pygame
from Entity.Player.player import Player
from Entity.Monster.monster import Monster
from Entity.Bullet.bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pew pew")

clock = pygame.time.Clock()

player = Player(320, 450)
monster = Monster(320,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Nhấn Enter để Player bắn
                player.shootBullet(Bullet)
    
    monster.auto_shoot()
    monster.move()
    player.update_bullets()
    monster.update_bullets()

    screen.fill((0, 0, 0))
    player.draw(screen)
    monster.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
