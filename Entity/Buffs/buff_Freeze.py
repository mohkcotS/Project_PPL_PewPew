import pygame
from Entity.Buffs.buff import Buff
class BuffFreeze(Buff):
    def __init__(self, x, y, direction, is_effect=False, freeze_duration=5000):
        super().__init__(x, y, direction, buff_type="freeze", image_path="src/assets/Buffs/Freeze.png")
        self.is_effect = is_effect
        self.spawn_time = pygame.time.get_ticks()
        self.freeze_duration = freeze_duration

    def is_expired(self):
        if not self.is_effect:
            return False
        return pygame.time.get_ticks() - self.spawn_time > self.freeze_duration

    def update(self):
        if not self.is_effect:
            super().update()

    def draw(self, screen):
        if self.is_effect:
            start = (self.x, self.y)
            end = self.get_end_point()
            temp_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            color = (0, 255, 255, 80)
            pygame.draw.line(temp_surface, color, start, end, 150)
            screen.blit(temp_surface, (0, 0))
        else:
            screen.blit(self.image, self.rect)

    def get_end_point(self):
        if self.direction == "mid":
            return (self.x, 0)
        elif self.direction == "mleft":
            return (self.x - 320, 0)
        elif self.direction == "left":
            return (self.x - 700, -100)
        elif self.direction == "right":
            return (self.x + 700, -100)
        elif self.direction == "mright":
            return (self.x + 320, 0)
        return (self.x, 0)
