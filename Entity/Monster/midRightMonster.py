from Entity.Monster.monster import Monster  # Import class Entity từ entity.py
import pygame
import math

class MidRightMonster(Monster):  # Kế thừa class Entity
    def __init__(self, x=585, y=0, direction="mid-right", color=(255, 255, 0)):
        super().__init__(x, y, direction, color)  

    def move(self):
        self.y += self.speed * math.sin(math.radians(67.3801))
        self.x -= self.speed * math.cos(math.radians(67.3801))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.draw_bullets(surface)