from Controller.direction import Direction
from Entity.Bullet.bullet import Bullet
import pygame

def KeyHandler(command, player):
    """Handle commands entered through the command box."""
    if not command:
        return  # Không xử lý nếu lệnh rỗng

    lastWord = command.strip().split()[-1]
    if "attack" in command:
        if "mleft" in command:
            player.direction = Direction.MID_LEFT_PLAYER
            player.shootBullet(Bullet, lastWord)
        elif "mright" in command:
            player.direction = Direction.MID_RIGHT_PLAYER
            player.shootBullet(Bullet, lastWord)
        elif "right" in command:
            player.direction = Direction.RIGHT_PLAYER
            player.shootBullet(Bullet, lastWord)
        elif "left" in command:
            player.direction = Direction.LEFT_PLAYER
            player.shootBullet(Bullet, lastWord)
        elif "mid" in command:
            player.direction = Direction.MID_PLAYER
            player.shootBullet(Bullet, lastWord)
    
    