import pygame

class Player:
    def __init__(self, x, y, color=(0, 255, 0), radius=30):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)