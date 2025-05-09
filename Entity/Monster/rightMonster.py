from Entity.Monster.monster import Monster  
import pygame
import math

class RightMonster(Monster): 
    def __init__(self, x=1100, y=0, direction="right", color=(255, 0, 0)):
        super().__init__(x, y, direction, color)  
        self.radius = 100
        avatar = pygame.image.load("src/assets/ship1.png").convert_alpha()
        self.avatar = pygame.transform.scale(avatar, (self.radius, self.radius))

    def move(self):
        self.y += self.speed * math.sin(math.radians(43))
        self.x -= self.speed * math.cos(math.radians(43))
    
    def draw(self, surface):
        angle = 133
        rotated_avatar = pygame.transform.rotate(self.avatar, angle)
        rect = rotated_avatar.get_rect(center=(self.x + self.radius // 2, self.y + self.radius // 2))
        surface.blit(rotated_avatar, rect.topleft)
        self.draw_bullets(surface)