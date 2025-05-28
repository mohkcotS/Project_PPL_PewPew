from abc import ABC, abstractmethod
from Entity.entity import Entity
import pygame
from Entity.Bullet.bullet import Bullet
from Utils.randomName import RandomName
import random

class Monster(Entity, ABC): 
    def __init__(self, x, y, direction,color=(255, 0, 0), radius=30, speed=0.2, health=100, isPlayer="false"):
        super().__init__(x, y, isPlayer, RandomName() ,color, radius, speed, direction)
        self.health = health
        self.last_shot = 0
        self.shoot_cooldown = 8000
        self.font = pygame.font.Font(None, 24)
        self.freeze_until = 0  

    def is_frozen_now(self):
        return pygame.time.get_ticks() < self.freeze_until

    @abstractmethod
    def move(self):
        pass  

    def auto_shoot(self):
        if self.is_frozen_now():
            return
        pu = random.choice(range(8000, 16001, 4000))
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot >= pu: 
            self.shootBullet(Bullet,self.name)
            self.last_shot = current_time

    @abstractmethod
    def draw(self, surface):
        pass