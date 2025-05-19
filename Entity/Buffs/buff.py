import pygame
from Entity.entity import Entity

class Buff(Entity):
    def __init__(self, x, y, direction, buff_type, image_path, ):
        super().__init__(x, y, isPlayer=False, radius=70)
        self.buff_type = buff_type
        self.dy = 0.3
        self.move_range = 10
        self.base_y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        self.direction = direction

    def update(self):
        self.y += self.dy
        if abs(self.y - self.base_y) > self.move_range:
            self.dy *= -1
        if(self.direction == "mid"):
            self.rect.center = (int(self.x), int(self.y) + 50)
        else:
            self.rect.center = (int(self.x) + 50, int(self.y) + 50)

    def draw(self, screen):
        screen.blit(self.image, self.rect)