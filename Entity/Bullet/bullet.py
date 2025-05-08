from Entity.entity import Entity  # Import class Entity từ entity.py
import pygame
import math
from  Controller.direction import Direction

class Bullet(Entity):
    def __init__(self, x, y, direction, color=(255, 255, 0), radius=5, speed=3.5):
        super().__init__(x, y, color, radius, speed)
        self.direction = direction

    def move(self):
        # Monster
        if self.direction == "right":
            self.y += self.speed * math.sin(math.radians(44))
            self.x -= self.speed * math.cos(math.radians(44))
        elif self.direction == "mid-right":
            self.y += self.speed * math.sin(math.radians(62))
            self.x -= self.speed * math.cos(math.radians(62))
        elif self.direction == "mid":
            self.y += self.speed
        elif self.direction == "mid-left":
            self.y += self.speed * math.sin(math.radians(62))
            self.x += self.speed * math.cos(math.radians(62))
        elif self.direction == "left":
            self.y += self.speed * math.sin(math.radians(44))
            self.x += self.speed * math.cos(math.radians(44))
        # Player
        elif self.direction == Direction.LEFT_PLAYER:
            self.y -= self.speed * math.sin(math.radians(44))
            self.x -= self.speed * math.cos(math.radians(44))
        elif self.direction == Direction.MID_LEFT_PLAYER:
            self.y -= self.speed * math.sin(math.radians(62))
            self.x -= self.speed * math.cos(math.radians(62))
        elif self.direction == Direction.MID_PLAYER:
            self.y -= self.speed 
        elif self.direction == Direction.MID_RIGHT_PLAYER:
            self.y -= self.speed * math.sin(math.radians(62))
            self.x += self.speed * math.cos(math.radians(62))
        elif self.direction == Direction.RIGHT_PLAYER:
            self.y -= self.speed * math.sin(math.radians(44))
            self.x += self.speed * math.cos(math.radians(44))
       

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)