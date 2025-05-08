from Entity.Monster.monster import Monster  
import pygame

class MidMonster(Monster): 
    def __init__(self, x=385, y=0, direction="mid", color=(255, 0, 0)):
        super().__init__(x, y, direction, color)  

    def move(self):
        self.y += self.speed 
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.draw_bullets(surface)