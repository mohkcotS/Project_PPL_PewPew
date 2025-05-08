from Entity.entity import Entity  # Import class Entity từ entity.py
import pygame
from Entity.Bullet.bullet import Bullet

class Monster(Entity):
    def __init__(self, x, y, color=(255, 0, 0), radius=30, speed=2, health=100):
        super().__init__(x, y, color, radius, speed)
        self.health = health
        self.last_shot = 0
        self.shoot_cooldown = 500
        self.direction = "mid"

    def move(self):
        self.y += self.speed

    def auto_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot >= self.shoot_cooldown:
            self.shootBullet(Bullet)
            self.last_shot = current_time

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        self.draw_bullets(surface)