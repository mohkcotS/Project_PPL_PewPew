import pygame
class Entity:
    def __init__(self, x, y, color=(0, 255, 0), radius=30, speed=2, direction="mid"):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed
        self.bullets = []
        self.direction = direction

    def move(self):
        self.y += self.speed 

    def shootBullet(self, bullet_class):
        bullet = bullet_class(
            x=self.x, 
            y=self.y, 
            color=(255, 255, 0), 
            radius=5, 
            speed=5,
            direction=self.direction 
        )
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
        self.bullets = [bullet for bullet in self.bullets if bullet.x < 640 + bullet.radius]

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    
    def draw_bullets(self, surface):
        for bullet in self.bullets:
            bullet.draw(surface)