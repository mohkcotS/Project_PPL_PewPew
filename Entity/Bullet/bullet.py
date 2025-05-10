import random
from Entity.entity import Entity
import pygame
import math
from Controller.direction import Direction

direction_angles = {
    "right": 137,
    "mid-right": 150,
    "mid": 180,
    "mid-left": 210,
    "left": 223,
    Direction.RIGHT_PLAYER: -43,
    Direction.MID_RIGHT_PLAYER: -30,
    Direction.MID_PLAYER: 0,
    Direction.MID_LEFT_PLAYER: 30,
    Direction.LEFT_PLAYER: 43
}

class Bullet(Entity):
    player_bullet_image = None
    monster_bullet_images = []

    @staticmethod
    def load_images():
        if Bullet.player_bullet_image is None:
            Bullet.player_bullet_image = pygame.image.load("src/assets/Bullet/01.png").convert_alpha()
            Bullet.monster_bullet_images = [
                pygame.image.load("src/assets/Bullet/01.png").convert_alpha(),
                pygame.image.load("src/assets/Bullet/02.png").convert_alpha(),
            ]

    def __init__(self, x, y, isPlayer, direction, color=(255, 255, 0), radius=5, speed=2.5):
        Bullet.load_images()

        super().__init__(x, y, direction, color, radius, speed)
        self.direction = direction
        self.color = color
        self.isPlayer = isPlayer

        if self.isPlayer == "true":
            original_image = Bullet.player_bullet_image
            self.speed = 5
        else:
            original_image = random.choice(Bullet.monster_bullet_images)

        angle = direction_angles.get(direction, 0)
        self.image = pygame.transform.rotate(original_image, angle)
        self.rect = self.image.get_rect(center=(x, y))

        if self.direction == "right":
            self.x -= 15
            self.y += 105
        elif self.direction == "left":
            self.x += 107
            self.y += 105
        elif self.direction == "mid-left":
            self.x += 75
            self.y += 105
        elif self.direction == "mid-right":
            self.x += 10
            self.y += 105

    def move(self):
        # Monster
        if self.direction == "right":
            self.y += self.speed * math.sin(math.radians(43))
            self.x -= self.speed * math.cos(math.radians(43))
        elif self.direction == "mid-right":
            self.y += self.speed * math.sin(math.radians(60))
            self.x -= self.speed * math.cos(math.radians(60))
        elif self.direction == "mid":
            self.y += self.speed
        elif self.direction == "mid-left":
            self.y += self.speed * math.sin(math.radians(60))
            self.x += self.speed * math.cos(math.radians(60))
        elif self.direction == "left":
            self.y += self.speed * math.sin(math.radians(43))
            self.x += self.speed * math.cos(math.radians(43))
        # Player
        elif self.direction == Direction.LEFT_PLAYER:
            self.y -= self.speed * math.sin(math.radians(43))
            self.x -= self.speed * math.cos(math.radians(43))
        elif self.direction == Direction.MID_LEFT_PLAYER:
            self.y -= self.speed * math.sin(math.radians(60))
            self.x -= self.speed * math.cos(math.radians(60))
        elif self.direction == Direction.MID_PLAYER:
            self.y -= self.speed 
        elif self.direction == Direction.MID_RIGHT_PLAYER:
            self.y -= self.speed * math.sin(math.radians(60))
            self.x += self.speed * math.cos(math.radians(60))
        elif self.direction == Direction.RIGHT_PLAYER:
            self.y -= self.speed * math.sin(math.radians(43))
            self.x += self.speed * math.cos(math.radians(43)) 
        
        self.rect.center = (self.x, self.y) 

    def draw(self, surface):
        surface.blit(self.image, self.rect)