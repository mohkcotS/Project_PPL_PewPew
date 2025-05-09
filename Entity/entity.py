from abc import ABC, abstractmethod
import pygame

class Entity(ABC):  # Kế thừa từ ABC để thành lớp trừu tượng
    def __init__(self, x, y, isPlayer, color=(0, 255, 0), radius=30, speed=2, direction="mid"):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed
        self.bullets = []
        self.direction = direction
        self.isPlayer = isPlayer
    
    @abstractmethod
    def draw(self, surface):
        pass  # Lớp con bắt buộc phải override
    
    def shootBullet(self, bullet_class):
        bullet = bullet_class(
            x=self.x, 
            y=self.y, 
            isPlayer=self.isPlayer,
            color=(255, 255, 0), 
            radius=5, 
            speed=5,
            direction=self.direction,
        )
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
        self.bullets = [bullet for bullet in self.bullets if bullet.x < 1200 + bullet.radius]
    
    def draw_bullets(self, surface):
        for bullet in self.bullets:
            bullet.draw(surface)