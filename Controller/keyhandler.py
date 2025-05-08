from Controller.direction import Direction
from Entity.Bullet.bullet import Bullet
import pygame

def KeyHandler(inputKey,player):
    if inputKey == pygame.K_a:  # Nhấn Enter để Player bắn
        player.direction = Direction.LEFT_PLAYER
        player.shootBullet(Bullet)
    elif inputKey == pygame.K_s:  # Nhấn Enter để Player bắn
        player.direction = Direction.MID_LEFT_PLAYER
        player.shootBullet(Bullet)
    elif inputKey == pygame.K_d:  # Nhấn Enter để Player bắn
        player.direction = Direction.MID_PLAYER
        player.shootBullet(Bullet)
    elif inputKey == pygame.K_f:  # Nhấn Enter để Player bắn
        player.direction = Direction.MID_RIGHT_PLAYER
        player.shootBullet(Bullet)
    elif inputKey == pygame.K_g:  # Nhấn Enter để Player bắn
        player.direction = Direction.RIGHT_PLAYER
        player.shootBullet(Bullet)