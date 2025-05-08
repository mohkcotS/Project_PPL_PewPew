import pygame
from Entity.entity import Entity

class Player(Entity):  # Kế thừa class Entity
    def __init__(self, x, y, color=(0, 0, 255), radius=30, speed=2, score=0):
        super().__init__(x, y, color, radius, speed)  # Gọi hàm __init__ của lớp cha (Entity)
        self.score = score  # Thêm thuộc tính riêng cho Player

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)  # Vẽ người chơi
        # Có thể vẽ thêm điểm số, tên, v.v.