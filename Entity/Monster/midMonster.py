from Entity.Monster.monster import Monster  
import pygame

class MidMonster(Monster): 
    def __init__(self, x=385, y=0, color=(255, 0, 0)):
        super().__init__(x, y, color)  

    def move(self):
        self.y += self.speed 

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)  