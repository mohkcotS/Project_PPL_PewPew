from abc import ABC, abstractmethod
from Entity.entity import Entity
import pygame

class Monster(Entity, ABC):  # Kế thừa từ Entity và ABC để thành lớp trừu tượng
    def __init__(self, x, y, color=(255, 0, 0), radius=30, speed=2, health=100):
        super().__init__(x, y, color)
        self.radius = radius
        self.speed = speed
        self.health = health

    @abstractmethod
    def move(self):
        pass  # Lớp con bắt buộc phải override

    @abstractmethod
    def draw(self, surface):
        pass  # Lớp con bắt buộc phải override
