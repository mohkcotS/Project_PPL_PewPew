from Entity.Monster.monster import Monster  # Import class Entity từ entity.py
import pygame
import math

class MidLeftMonster(Monster):  # Kế thừa class Entity
    def __init__(self, x=260, y=0, direction="mid-left", color=(255, 255, 0)):
        super().__init__(x, y, direction, color)  
        self.radius = 100
        avatar = pygame.image.load("src/assets/ship4.png").convert_alpha()
        self.avatar = pygame.transform.scale(avatar, (self.radius, self.radius))

    def move(self):
        self.y += self.speed * math.sin(math.radians(60))
        self.x += self.speed * math.cos(math.radians(60))

    def draw(self, surface):
        angle = 210
        rotated_avatar = pygame.transform.rotate(self.avatar, angle)
        rect = rotated_avatar.get_rect(center=(self.x + self.radius // 2, self.y + self.radius // 2))
        surface.blit(rotated_avatar, rect.topleft)
        self.draw_bullets(surface)