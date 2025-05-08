from Entity.entity import Entity  # Import class Entity từ entity.py
import pygame

class Monster(Entity):  # Kế thừa class Entity
    def __init__(self, x, y, color=(255, 0, 0), radius=30, speed=2, health=100):
        super().__init__(x, y, color, radius, speed)  # Gọi hàm __init__ của lớp cha (Entity)
        self.health = health  # Thêm thuộc tính riêng cho Monster

    def move(self):
        self.y += self.speed  # Có thể tùy chỉnh lại phương thức move nếu cần

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)  # Vẽ quái vật
        # Thêm vẽ thông tin khác nếu cần
