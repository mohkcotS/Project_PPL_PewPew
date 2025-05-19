import pygame
from Entity.Buffs.buff import Buff

class BuffLazer(Buff):
    def __init__(self, x, y, direction, is_effect=False):
        super().__init__(x, y, direction, buff_type="lazer", image_path="src/assets/Buffs/Laser.png")
        self.is_effect = is_effect
        self.spawn_time = pygame.time.get_ticks()
        self.duration = 300

        if is_effect:
            self.image = pygame.image.load("src/assets/Buffs/LaserEffect_1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (400, 1000)) 
            self.angle = self.get_rotation_angle(direction)
            self.y -= 470
            if self.direction == "right":
                self.x += 350
                self.y += 160
            elif self.direction == "mright":
                self.x += 240
                self.y += 80
            elif self.direction == "mleft":
                self.x -= 230
                self.y += 80
            elif self.direction == "left":
                self.x -= 350
                self.y += 160

    def is_expired(self):
        if not self.is_effect:
            return False
        return pygame.time.get_ticks() - self.spawn_time > self.duration

    def update(self):
        if not self.is_effect:
            super().update()

    def draw(self, screen):
        if self.is_effect:
            rotated = pygame.transform.rotate(self.image, self.angle)
            rect = rotated.get_rect(center=(self.x, self.y))
            screen.blit(rotated, rect.topleft)
        else:
            screen.blit(self.image, self.rect)

    def get_rotation_angle(self, direction):
        angles = {
            "mid": 0,
            "mleft": 28,
            "left": 46,
            "mright": -33,
            "right": -46,
        }
        return angles.get(direction, 0)