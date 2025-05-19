from Entity.Monster.monster import Monster  
import pygame

class MidMonster(Monster): 
    def __init__(self, x=600, y=0, direction="mid", color=(255, 0, 0)):
        super().__init__(x, y, direction, color)  
        self.radius = 100
        avatar = pygame.image.load("src/assets/ship3.png").convert_alpha()
        self.avatar = pygame.transform.scale(avatar, (self.radius, self.radius))

    def move(self):
        if self.is_frozen_now():
            return
        self.y += self.speed 
    
    def draw(self, surface):
        angle = 180
        rotated_avatar = pygame.transform.rotate(self.avatar, angle)  # Xoay 180 độ
        rect = rotated_avatar.get_rect(center=(self.x, self.y))
        surface.blit(rotated_avatar, rect.topleft)

        text = self.font.render(self.name, True, (255, 255, 255))  
        text_rect = text.get_rect(center=(self.x, self.y + self.radius/2)) 
        surface.blit(text, text_rect)

        self.draw_bullets(surface)
        