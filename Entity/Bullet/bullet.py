from Entity.entity import Entity  # Import class Entity từ entity.py
import pygame

class Bullet(Entity):  # Kế thừa class Entity
    def __init__(self, x, y, color=(255, 255, 0), radius=5, speed=5):
        super().__init__(x, y, color, radius, speed)  # Gọi hàm __init__ của lớp cha (Entity)

    def move(self):
        self.x += self.speed  # Bullet di chuyển theo trục x

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)  # Vẽ viên đạn
