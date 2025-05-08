from Entity.Monster.monster import Monster  
import pygame
import math

class RightMonster(Monster): 
    def __init__(self, x=770, y=0, direction="right", color=(255, 0, 0)):
        super().__init__(x, y, direction, color)  

    def move(self):
        self.y += self.speed * math.sin(math.radians(50.1944))
        self.x -= self.speed * math.cos(math.radians(50.1944))
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.draw_bullets(surface)