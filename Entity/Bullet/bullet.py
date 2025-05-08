from Entity.entity import Entity  # Import class Entity từ entity.py
import pygame
import math

class Bullet(Entity):
    def __init__(self, x, y, direction, color=(255, 255, 0), radius=5, speed=5):
        super().__init__(x, y, color, radius, speed)
        self.direction = direction

    def move(self):
        if self.direction == "right":
            self.y += self.speed * math.sin(math.radians(50.1944))
            self.x -= self.speed * math.cos(math.radians(50.1944))
        elif self.direction == "mid-right":
            self.y += self.speed * math.sin(math.radians(67.3801))
            self.x -= self.speed * math.cos(math.radians(67.3801))
        elif self.direction == "mid":
            self.y += self.speed
        elif self.direction == "mid-left":
            self.y += self.speed * math.sin(math.radians(67.3801))
            self.x += self.speed * math.cos(math.radians(67.3801))
        elif self.direction == "left":
            self.y += self.speed * math.sin(math.radians(50.1944))
            self.x += self.speed * math.cos(math.radians(50.1944))
        # Player
        elif self.direction == "mid_player":
            self.y -= self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)