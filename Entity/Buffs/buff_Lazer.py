import pygame
from Entity.Buffs.buff import Buff

class BuffLazer(Buff):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction, buff_type="lazer", image_path="src/assets/Buffs/Laser.png")