from abc import ABC, abstractmethod
from Entity.entity import Entity
import pygame
from Entity.Bullet.bullet import Bullet


class Monster(Entity, ABC): 
    def __init__(self, x, y, direction, color=(255, 0, 0), radius=30, speed=1, health=100):
        super().__init__(x, y, color)
        self.radius = radius
        self.speed = speed
        self.health = health
        self.last_shot = 0
        self.shoot_cooldown = 2000
        self.direction = direction

    @abstractmethod
    def move(self):
        pass  

    def auto_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot >= self.shoot_cooldown:
            self.shootBullet(Bullet)
            self.last_shot = current_time

    @abstractmethod
    def draw(self, surface):
        pass