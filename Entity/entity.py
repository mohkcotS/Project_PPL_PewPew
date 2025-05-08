import pygame
class Entity:
    def __init__(self, x, y, color=(0, 255, 0), radius=30, speed=2):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed

    def move(self):
        self.y += self.speed 

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)