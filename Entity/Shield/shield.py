import pygame
from Entity.entity import Entity

class Shield(Entity):
    def __init__(self, x = 600, y=450, direction="mid", imagePath="src/assets/Shield/shield.png"):
        super().__init__(x, y, isPlayer=False, radius=5, direction=direction)

        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 35)) 
        self.angle = self.get_rotation_angle(direction)
        
        if direction == "right":
            self.x += 90
            self.y += 45
        elif direction == "mright":
            self.x += 55
            self.y += 10
        elif direction == "mleft":
            self.x -= 55
            self.y += 10
        elif direction == "left":
            self.x -= 90
            self.y += 45
        

        self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(rotated, rect.topleft)

    def get_rotation_angle(self, direction):
        angles = {
            "mid": 0,
            "mleft": 28,
            "left": 46,
            "mright": -28,
            "right": -46,
        }
        return angles.get(direction, 0)
