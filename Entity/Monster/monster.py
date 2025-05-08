from abc import ABC, abstractmethod
from Entity.entity import Entity
import pygame
from Entity.Bullet.bullet import Bullet


class Monster(Entity, ABC):  # Kế thừa từ Entity và ABC để thành lớp trừu tượng
    def __init__(self, x, y, color=(255, 0, 0), radius=30, speed=2, health=100):
        super().__init__(x, y, color)
        self.radius = radius
        self.speed = speed
        self.health = health

    @abstractmethod
    def move(self):
        pass  # Lớp con bắt buộc phải override

    def auto_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot >= self.shoot_cooldown:
            self.shootBullet(Bullet)
            self.last_shot = current_time

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.draw_bullets(surface)

