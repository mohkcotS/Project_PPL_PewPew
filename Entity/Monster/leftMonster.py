from Entity.Monster.monster import Monster  
import pygame
import math

class LeftMonster(Monster): 
    def __init__(self, x=30, y=0, direction="left", color=(255, 0, 0)):
        super().__init__(x, y, direction, color)  

    def move(self):
        self.y += self.speed * math.sin(math.radians(44))
        self.x += self.speed * math.cos(math.radians(44))
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.draw_bullets(surface)