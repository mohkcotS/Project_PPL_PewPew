import pygame
from Entity.entity import Entity

class Player(Entity):
    def __init__(self, x=400, y=445, color=(0, 0, 255), radius=30, speed=5, score=0, direction ="mid_player"):
        super().__init__(x, y, color, radius, speed, direction)
        self.score = score

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.draw_bullets(surface)