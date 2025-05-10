from Controller.direction import Direction
from Entity.Bullet.bullet import Bullet
import pygame

def KeyHandler(command, player):
    """Handle commands entered through the command box."""
    if not command:
        return  # Không xử lý nếu lệnh rỗng

    command = command.lower()  # Chuyển thành chữ thường để dễ so sánh
    if command == "a":
        player.direction = Direction.LEFT_PLAYER
        player.shootBullet(Bullet)
    elif command == "s":
        player.direction = Direction.MID_LEFT_PLAYER
        player.shootBullet(Bullet)
    elif command == "d":
        player.direction = Direction.MID_PLAYER
        player.shootBullet(Bullet)
    elif command == "f":
        player.direction = Direction.MID_RIGHT_PLAYER
        player.shootBullet(Bullet)
    elif command == "g":
        player.direction = Direction.RIGHT_PLAYER
        player.shootBullet(Bullet)